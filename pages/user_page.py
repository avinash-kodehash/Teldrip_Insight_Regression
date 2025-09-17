from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class User(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    USER_TABLE = (By.CSS_SELECTOR, "")
    FIRST_CELL = (By.XPATH, "//tr[1]//td[2]")

    def is_user_table_visible(self):
        return self.element_displayed(self.USER_TABLE)

    def is_table_data_present(self):
        self.wait_for_non_empty_text(self.FIRST_CELL)
        return self.driver.find_element(*self.FIRST_CELL).text