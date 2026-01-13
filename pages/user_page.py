from selenium.webdriver.common.by import By
from constants.constants import Constant
from pages.base_page import BasePage

class User(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    USER_TABLE = (By.CSS_SELECTOR, "")
    FIRST_CELL = (By.XPATH, "//tr[1]//td[2]")
    ADD_NEW_USER_BUTTON = (By.CSS_SELECTOR, "p[aria-label='Add new user'] button[type='button']")
    ADD_USER_MANUALLY_BUTTON = (By.XPATH, "//button[normalize-space()='Add User Manually']")
    ADD_USER_MANUALLY_SELECT_ROLE = (By.XPATH, "//div[@placeholder='Select Role']")
    ADD_USER_MANUALLY_SELECT_ROLE_LIST = (By.XPATH, "//li")
    ADD_USER_MANUALLY_SELECT_ROLE_ADVERTISER = (By.XPATH, "//li[normalize-space(text())='Advertiser']")
    ADD_USER_MANUALLY_SELECT_ROLE_PUBLISHER = (By.XPATH, "//li[normalize-space(text())='Publisher']")
    ADD_USER_MANUALLY_FIRST_NAME = (By.XPATH, "//input[@placeholder='First Name']")
    ADD_USER_MANUALLY_LAST_NAME = (By.XPATH, "//input[@placeholder=' Last Name']")
    ADD_USER_MANUALLY_MOB_NO = (By.XPATH, "//input[@placeholder=' Mobile Number ']")
    ADD_USER_MANUALLY_COUNTRY_DROPDOWN = (By.CSS_SELECTOR, ".MuiBox-root.css-18u0snp")
    ADD_USER_MANUALLY_COUNTRY_LIST = (By.XPATH, "//li")
    ADD_USER_MANUALLY_EMAIL = (By.XPATH, "//input[@placeholder='Email ID']")
    ADD_USER_MANUALLY_NEXT_BTN_1 = (By.XPATH, "//button[normalize-space()='Next']")
    ADD_USER_MANUALLY_COMPANY_NAME = (By.XPATH,"//input[@placeholder=' Company Name']")
    ADD_USER_MANUALLY_COMPANY_ADDRESS = (By.XPATH,"//input[@placeholder=' Company Address  ']")
    ADD_USER_MANUALLY_COMPANY_WEBSITE = (By.XPATH,"//input[@placeholder=' Company Website ']")
    ADD_USER_MANUALLY_NEXT_BTN_2 = (By.XPATH, "//button[normalize-space()='Next']")
    ADD_USER_MANUALLY_COMPANY_SIZE_DROPDOWN = (By.CSS_SELECTOR, "input[id=':r3k:']")
    ADD_USER_MANUALLY_ADD_USER_BTN = (By.XPATH, "//button[normalize-space()='Add user']")
    ADD_USER_MANUALLY_INDUSTRY_DROPDOWN = ()
    USER_ADDED_SUCCESSFULLY_TEXT = (By.XPATH, "//p[normalize-space(text())='User Added Successfully']")
    INVITE_USER_EMAIL = (By.XPATH, "//input[@placeholder='Enter user email']")
    INVITE_USER_BUTTON = (By.XPATH, "//p[@aria-label='Add new user']//button[@type='button']")
    INVITE_USER_SEND_INVITE_BUTTON = (By.XPATH, "//button[normalize-space()='Send invite']")

    def is_user_table_visible(self):
        self.logger.info("Checking if user table is visible")
        return self.element_displayed(self.USER_TABLE)

    def is_table_data_present(self):
        self.logger.info("Checking if user table data is present")
        self.wait_for_non_empty_text(self.FIRST_CELL)
        data = self.driver.find_element(*self.FIRST_CELL).text
        self.logger.info(f"User table data present: {data}")
        return data

    def select_country(self):
        # self.logger.info(f"Selecting country: {Constant.USER_COUNTRY}")
        # self.do_click(self.ADD_USER_MANUALLY_COUNTRY_DROPDOWN)
        # countries = self.driver.find_elements(*self.ADD_USER_MANUALLY_COUNTRY_LIST)
        # for country in countries:
        #     if country.text == Constant.USER_COUNTRY:
        #         country.click()
        #         self.logger.info(f"Country {Constant.USER_COUNTRY} selected successfully")
        #         break
        self.fill(self.ADD_USER_MANUALLY_MOB_NO, Constant.USER_COUNTRY)

    def select_role(self):
        if Constant.USER_ROLE.lower() == "Advertiser":
            self.do_click(self.ADD_USER_MANUALLY_SELECT_ROLE_ADVERTISER)
        elif Constant.USER_ROLE.lower() == "publisher":
            self.do_click(self.ADD_USER_MANUALLY_SELECT_ROLE_PUBLISHER)
        else:
            raise ValueError(f"Role {Constant.USER_ROLE} not found")