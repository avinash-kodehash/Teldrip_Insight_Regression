import requests
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from utils.logger import Logger

class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.logger = Logger.get_logger(self.__class__.__name__)

    def do_click(self,by_locator):
        try:
            self.logger.info(f"Clicking element: {by_locator}")
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(by_locator)).click()
            self.logger.debug(f"Successfully clicked element: {by_locator}")
        except Exception as e:
            self.logger.error(f"Failed to click element: {by_locator}. Error: {str(e)}")
            raise

    def fill(self,by_locator,text):
        try:
            self.logger.info(f"Filling element: {by_locator} with text: {'*' * len(str(text)) if 'password' in str(by_locator).lower() else text}")
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located(by_locator)).send_keys(text)
            self.logger.debug(f"Successfully filled element: {by_locator}")
        except Exception as e:
            self.logger.error(f"Failed to fill element: {by_locator}. Error: {str(e)}")
            raise

    def element_displayed(self,by_locator):
        try:
            self.logger.debug(f"Checking if element is displayed: {by_locator}")
            result = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).is_displayed()
            self.logger.debug(f"Element displayed status for {by_locator}: {result}")
            return result
        except Exception as e:
            self.logger.error(f"Element not displayed: {by_locator}. Error: {str(e)}")
            raise

    def get_element_text(self,locator):
        try:
            self.logger.debug(f"Getting text from element: {locator}")
            text = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator)).text
            self.logger.debug(f"Retrieved text from {locator}: {text}")
            return text
        except Exception as e:
            self.logger.error(f"Failed to get text from element: {locator}. Error: {str(e)}")
            raise

    def take_element_screenshot(self,locator,file_path):
        try:
            self.logger.info(f"Taking screenshot of element: {locator} to {file_path}")
            element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator))
            element.screenshot(file_path)
            self.logger.debug(f"Screenshot saved successfully: {file_path}")
        except Exception as e:
            self.logger.error(f"Failed to take screenshot of element: {locator}. Error: {str(e)}")
            raise

    def take_full_screenshot(self,file_path):
        try:
            self.logger.info(f"Taking full page screenshot to: {file_path}")
            self.driver.save_screenshot(file_path)
            self.logger.debug(f"Full screenshot saved successfully: {file_path}")
        except Exception as e:
            self.logger.error(f"Failed to take full screenshot. Error: {str(e)}")
            raise

    def scroll_to_element(self,locator):
        try:
            self.logger.debug(f"Scrolling to element: {locator}")
            element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator))
            self.driver.execute_script("arguments[0].scrollIntoView(true);",element)
            self.logger.debug(f"Successfully scrolled to element: {locator}")
        except Exception as e:
            self.logger.error(f"Failed to scroll to element: {locator}. Error: {str(e)}")
            raise

    def scroll(self,length):
        try:
            self.logger.debug(f"Scrolling page by {length} pixels")
            self.driver.execute_script(f"window.scrollBy(0, {length});")
        except Exception as e:
            self.logger.error(f"Failed to scroll page. Error: {str(e)}")
            raise

    def javascript_executor(self,value):
        try:
            self.logger.debug(f"Executing JavaScript: {value}")
            self.driver.execute_script(value)
        except Exception as e:
            self.logger.error(f"Failed to execute JavaScript. Error: {str(e)}")
            raise

    def zoom_control(self, zoom_level):
        try:
            self.logger.info(f"Setting zoom level to: {zoom_level}%")
            self.driver.execute_script(f"document.body.style.zoom='{zoom_level}%'")
        except Exception as e:
            self.logger.error(f"Failed to set zoom level. Error: {str(e)}")
            raise

    def extract_table_as_dataframe(self, table_locator, exclude_last_n=0, drop_sno=True, normalize_spaces=True):
        self.logger.info(f"Extracting table data from: {table_locator}")
        table = self.driver.find_element(*table_locator)

        # Headers
        headers = [h.text.strip() for h in table.find_elements(By.CSS_SELECTOR, "thead th")]
        if exclude_last_n > 0:
            headers = headers[:-exclude_last_n]

        # Rows
        rows = table.find_elements(By.CSS_SELECTOR, "tbody tr")
        data = []
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            #time.sleep(5)
            row_data = [c.text.strip() for c in cols]
            if exclude_last_n > 0:
                row_data = row_data[:-exclude_last_n]
            data.append(row_data)

        df = pd.DataFrame(data, columns=headers)

        # Drop S.no column if present
        if drop_sno and df.shape[1] > 0:
            df = df.drop(df.columns[0], axis=1)
        
        self.logger.info(f"Extracted table with {len(df)} rows and {len(df.columns)} columns")
        return df


    def extract_all_pages_as_dataframe(self, table_locator, next_button_locator,
                                       exclude_last_n=0, drop_sno=True, normalize_spaces=True,
                                       wait_after_click=10):
        """
        Extracts all paginated table data into one DataFrame.
        """
        self.logger.info("Starting extraction of paginated table data")
        all_dfs = []
        page_count = 0

        while True:
            # Extract current page
            df_page = self.extract_table_as_dataframe(
                table_locator,
                exclude_last_n=exclude_last_n,
                drop_sno=drop_sno,
                normalize_spaces=normalize_spaces
            )
            all_dfs.append(df_page)
            page_count += 1
            self.logger.debug(f"Extracted page {page_count}")
            try:
                next_button = self.driver.find_element(*next_button_locator)

                disabled_attr = next_button.get_attribute("disabled")
                if disabled_attr is not None or not next_button.is_enabled():
                    break

                self.do_click(next_button_locator)
                time.sleep(wait_after_click)

            except Exception:
                # If no next button or can't click, stop
                break

        if all_dfs:
            result_df = pd.concat(all_dfs, ignore_index=True)
            self.logger.info(f"Extracted total of {len(result_df)} rows from {page_count} pages")
            return result_df
        else:
            self.logger.warning("No data extracted from paginated table")
            return pd.DataFrame()

    def wait_for_table_to_load(self,locator):
        #assert isinstance(self.get_element_text(locator).strip(), str)
        return self.get_element_text(locator)

    def wait_for_non_empty_text(self, locator, timeout=15):
        try:
            return WebDriverWait(self.driver, timeout).until(
                lambda d: d.find_element(*locator).text.strip() != ""
        )
        except TimeoutException:
            raise AssertionError

    def get_elements_text_as_list(self, locator_string):
        elements = self.driver.find_elements(By.XPATH, locator_string)
        return [el.text.strip() for el in elements]

    def get_elements_as_list(self, locator):
        return self.driver.find_elements(*locator)

    def clear_input_field(self, locator):
        try:
            self.logger.debug(f"Clearing input field: {locator}")
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located(locator)).clear()
        except Exception as e:
            self.logger.error(f"Failed to clear input field: {locator}. Error: {str(e)}")
            raise

    def js_click(self, locator):
        try:
            self.logger.info(f"JavaScript clicking element: {locator}")
            element = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].click();", element)
            self.logger.debug(f"Successfully JS clicked element: {locator}")
        except Exception as e:
            self.logger.error(f"Failed to JS click element: {locator}. Error: {str(e)}")
            raise

def generate_token():
    logger = Logger.get_logger("APIHelper")
    try:
        logger.info("Generating authentication token")
        body = {"email":"meghna.c@kodehash.com","password":"KODEhash@000"}
        response = requests.post("https://admin.teldrip.com/api/login", json=body)
        logger.info("Authentication token generated successfully")
        return response.json()["access_token"]
    except Exception as e:
        logger.error(f"Failed to generate token. Error: {str(e)}")
        raise




