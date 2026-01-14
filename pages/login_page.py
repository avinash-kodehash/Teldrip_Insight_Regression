from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.dashboard_page import DashBoard


class LoginPage(BasePage):

    EMAIL = (By.XPATH,"//input[@placeholder='Enter Your Email ID']")
    PASSWORD = (By.XPATH,"//input[@placeholder='Enter Password']")
    LOGIN_BUTTON = (By.XPATH,"//button[normalize-space()='Login']")
    OTP_BUTTON=(By.XPATH,"//input[@class ='otp_input text-black']")
    VERIFY_BUTTON =(By.XPATH,"//button[@type='button']")
    TRUSTED_DEVICE_BUTTON =(By.XPATH,"(//button[@type ='button'])[5]")

    EMPTY_EMAIL_ERR_MSG = (By.CSS_SELECTOR, ".MuiTypography-root.MuiTypography-body1.css-1r94qnl")
    EMPTY_PASS_ERR_MSG = (By.CSS_SELECTOR, ".MuiTypography-root.MuiTypography-body1.css-1r94qnl'")
    OTP_INPUT_1 = (By.XPATH, "//input[@aria-label='Please enter OTP character 1']")
    OTP_INPUT_2 = (By.XPATH, "//input[@aria-label='Please enter OTP character 2']")
    OTP_INPUT_3 = (By.XPATH, "//input[@aria-label='Please enter OTP character 3']")
    OTP_INPUT_4 = (By.XPATH, "//input[@aria-label='Please enter OTP character 4']")
    OTP_INPUT_5 = (By.XPATH, "//input[@aria-label='Please enter OTP character 5']")
    OTP_INPUT_6 = (By.XPATH, "//input[@aria-label='Please enter OTP character 6']")
    VERIFY_OTP_BUTTON = (By.XPATH, "//button[normalize-space()='Verify']")
    BTN_TRUST_DEVICE = (By.XPATH, "//span[normalize-space()='Trust Device']")

    def __init__(self, driver):
        super().__init__(driver)

    def do_login(self,username,password):
        self.logger.info(f"Performing login with username: {username}")
        self.fill(self.EMAIL,username)
        self.fill(self.PASSWORD,password)
        self.do_click(self.LOGIN_BUTTON)
        self.fill(self.OTP_INPUT_1, "6")
        self.fill(self.OTP_INPUT_2, "6")
        self.fill(self.OTP_INPUT_3, "6")
        self.fill(self.OTP_INPUT_4, "6")
        self.fill(self.OTP_INPUT_5, "6")
        self.fill(self.OTP_INPUT_6, "6")
        self.do_click(self.VERIFY_OTP_BUTTON)
        self.do_click(self.BTN_TRUST_DEVICE)
        self.logger.info("Login credentials submitted successfully")

    def is_login_successful(self):
        self.logger.info("Checking if login was successful")
        db = DashBoard(self.driver)
        try:
            result = db.element_displayed(db.DASHBOARD_TEXT)
            self.logger.info(f"Login success check result: {result}")
            return result
        except Exception as e:
            self.logger.error(f"Login failed: {str(e)}")
            return False

