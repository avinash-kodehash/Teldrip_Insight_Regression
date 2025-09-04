from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    EMAIL = (By.ID,":r0:")
    PASSWORD = (By.ID,":r1:")
    LOGIN_BUTTON = (By.XPATH,"//button[normalize-space()='Login']")


    def __init__(self, driver):
        super().__init__(driver)

    def do_login(self,username,password):
        self.fill(self.EMAIL,username)
        self.fill(self.PASSWORD,password)
        self.do_click(self.LOGIN_BUTTON)

