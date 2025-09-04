from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Advertiser(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    ADVERTISER_TABLE = (By.CSS_SELECTOR, ".text-sm.text-primary-500")

    def is_advertiser_table_visible(self):
        return self.element_displayed(self.ADVERTISER_TABLE)

