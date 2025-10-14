from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.dashboard_page import DashBoard


class LoginPage(BasePage):

    EMAIL = (By.XPATH,"//input[@placeholder='Enter Your Email ID']")
    PASSWORD = (By.XPATH,"//input[@placeholder='Enter Password']")
    LOGIN_BUTTON = (By.XPATH,"//button[normalize-space()='Login']")
    EMPTY_EMAIL_ERR_MSG = (By.CSS_SELECTOR, ".MuiTypography-root.MuiTypography-body1.css-1r94qnl")
    EMPTY_PASS_ERR_MSG = (By.CSS_SELECTOR, ".MuiTypography-root.MuiTypography-body1.css-1r94qnl'")

    def __init__(self, driver):
        super().__init__(driver)

    def do_login(self,username,password):
        self.fill(self.EMAIL,username)
        self.fill(self.PASSWORD,password)
        self.do_click(self.LOGIN_BUTTON)

    def is_login_successful(self):
        db = DashBoard(self.driver)
        try:
            return db.element_displayed(db.DASHBOARD_TEXT)
        except:
            return False

