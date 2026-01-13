from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Profile(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    PROFILE_BTN = (By.XPATH, "//p[@aria-label='Profile']")
    PROFILE_SUB_BTN = (By.XPATH, "//button[normalize-space()='Profile']")
    PROFILE_NAME = (By.XPATH, "//li[normalize-space()='Name']")
    PROFILE_EMAIL = (By.XPATH, "//li[normalize-space()='Email ID']")
    PROFILE_MOBILE = (By.XPATH, "//li[normalize-space()='Mobile']")
    PROFILE_OFFICE_ADDRESS = (By.XPATH, "//li[normalize-space()='Office Address']")
    PROFILE_BILLING_ADDRESS = (By.XPATH, "//li[normalize-space()='Billing Address']")
    PROFILE_COMPANY_NAME = (By.XPATH, "//li[normalize-space()='Company Name']")
    PROFILE_EDIT_BUTTON = (By.XPATH, "/html/body/div[1]/div[1]/div/div/div[2]/div[2]/div/section[2]/div[1]/div/button")
    VERIFY_BTN = (By.XPATH, "//button[normalize-space()='Verify']")
    UPGRADE_PLAN_BTN = (By.XPATH, "//a[normalize-space()='Upgrade Plan']")
    UPGRADE_PLAN_TEXT = (By.XPATH, "(//p[@class='MuiTypography-root MuiTypography-body1 pricing_heading text--highlight-xl css-1r94qnl'])[1]")
    INVALID_EMAIL_ERR_MSG = (By.XPATH, "//div[contains(text(),'Please enter valid email id')]")
    SVG_MOBILE_ICON = (By.XPATH, "//button[@aria-label='Select country']")
    PROFILE_EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Enter Email ID']")
    PROFILE_NAME_INPUT = (By.XPATH, "//input[@placeholder='Enter Name']")
    PROFILE_SAVE_BTN = (By.XPATH, "//button[normalize-space()='Save Changes']")
    PROFILE_NAME_ERROR_MSG = (By.XPATH, "//div[contains(text(),'Name is required.')]")
