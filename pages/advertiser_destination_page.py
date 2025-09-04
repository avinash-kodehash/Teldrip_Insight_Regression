from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AdvertiserDestination(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    DESTINATION_TABLE = (By.CSS_SELECTOR,".text-sm.text-primary-500")

    def is_destination_table_visible(self):
        return self.element_displayed(self.DESTINATION_TABLE)
