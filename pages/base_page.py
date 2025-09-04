import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def do_click(self,by_locator):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(by_locator)).click()

    def fill(self,by_locator,text):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(by_locator)).send_keys(text)

    def element_displayed(self,by_locator):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).is_displayed()

    def get_element_text(self,locator):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator)).text

    def take_element_screenshot(self,locator,file_path):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator))
        element.screenshot(file_path)

    def take_full_screenshot(self,file_path):
        self.driver.save_screenshot(file_path)

    def scroll_to_element(self,locator):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);",element)

    def scroll(self,length):
        self.driver.execute_script(f"window.scrollBy(0, {length});")

    def javascript_executor(self,value):
        self.driver.execute_script(value)

    def zoom_control(self, zoom_level):
        self.driver.execute_script(f"document.body.style.zoom='{zoom_level}%'")

    def extract_table_as_dataframe(self, table_locator, exclude_last_n=0, drop_sno=True, normalize_spaces=True):
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
            row_data = [c.text.strip() for c in cols]
            if exclude_last_n > 0:
                row_data = row_data[:-exclude_last_n]
            data.append(row_data)

        df = pd.DataFrame(data, columns=headers)

        # Drop S.no column if present
        if drop_sno and 'S.no' in df.columns:
            df = df.drop(columns=['S.no'])
        return df

    def wait_for_table_to_load(self,locator):
        assert isinstance(self.get_element_text(locator).strip(), str)

def generate_token():
    body = {"email":"meghna.c@kodehash.com","password":"#120Test#"}
    response = requests.post("https://admin.teldrip.com/api/login", json=body)
    return response.json()["access_token"]




