from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Offer(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    OFFER_TABLE = (By.CSS_SELECTOR, ".text-sm.text-primary-500")
    FIRST_CELL = (By.XPATH, "//tr[1]//td[2]")

    def is_offer_table_visible(self):
        return self.element_displayed(self.OFFER_TABLE)

    def is_table_data_present(self):
        self.wait_for_non_empty_text(self.FIRST_CELL)
        return self.driver.find_element(*self.FIRST_CELL).text