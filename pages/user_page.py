from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class User(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    USER_TABLE = (By.CSS_SELECTOR, "")

    def is_user_table_visible(self):
        return self.element_displayed(self.USER_TABLE)