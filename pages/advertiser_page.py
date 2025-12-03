from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Advertiser(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    ADVERTISER_TABLE = (By.CSS_SELECTOR, ".text-sm.text-primary-500")
    FIRST_CELL = (By.XPATH, "//tr[1]//td[2]")

    def is_advertiser_table_visible(self):
        self.logger.info("Checking if advertiser table is visible")
        return self.element_displayed(self.ADVERTISER_TABLE)

    def is_table_data_present(self):
        self.logger.info("Checking if advertiser table data is present")
        self.wait_for_non_empty_text(self.FIRST_CELL)
        data = self.driver.find_element(*self.FIRST_CELL).text
        self.logger.info(f"Advertiser table data present: {data}")
        return data

