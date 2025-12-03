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
    PROFILE_EDIT_BUTTON = (By.XPATH, "(//button[contains(@class,'inline-flex items-center justify-center rounded-md font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 disabled:opacity-90 disabled:pointer-events-none border border-white rounded-[4px] lg:w-full py-2 px-3 mt-8')])[1]")
    VERIFY_BTN = (By.XPATH, "//button[normalize-space()='Verify']")
    UPGRADE_PLAN_BTN = (By.XPATH, "//a[normalize-space()='Upgrade Plan']")
    UPGRADE_PLAN_TEXT = (By.XPATH, "(//p[@class='MuiTypography-root MuiTypography-body1 pricing_heading text--highlight-xl css-1r94qnl'])[1]")
