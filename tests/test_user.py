from constants.constants import Constant
from pages.dashboard_page import DashBoard
from pages.login_page import LoginPage
from pages.user_page import User
from utils.logger import Logger
from faker import Faker
from utils.temp_mail_helper import TempMailHelper
import requests

faker = Faker()

logger = Logger.get_logger(__name__)

def test_user_table_visibility(driver):
    logger.info("Starting test: _user_table_visibility")
    lp = LoginPage(driver)
    
    logger.info("Step 1: Performing login")
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    
    logger.info("Step 2: Verifying dashboard is displayed")
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    
    logger.info("Step 3: Navigating to User section")
    db.click_advertiser_ele()
    db.do_click(db.USER_TAB)
    
    logger.info("Step 4: Verifying user table data is present")
    u = User(driver)
    #time.sleep(4)
    assert isinstance(u.is_table_data_present(), str),"Table data not present"
    logger.info("Test completed successfully: _user_table_visibility")

def test_add_user_manually(driver):
    first_name = faker.first_name()
    last_name = faker.last_name()
    email = f"{first_name}.{last_name}@yopmail.com"
    company = faker.company()
    company_address = faker.address()
    company_website = faker.url()
    logger.info("Starting test: test_add_user_manually")
    lp = LoginPage(driver)
    db = DashBoard(driver)
    u = User(driver)
    logger.info("Step 1: Performing login")
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    logger.info("Step 2: Verifying dashboard is displayed")
    db.element_displayed(db.DASHBOARD_TEXT)
    db.do_click(db.USER_TAB)
    u.do_click(u.ADD_NEW_USER_BUTTON)
    u.do_click(u.ADD_USER_MANUALLY_BUTTON)
    u.do_click(u.ADD_USER_MANUALLY_SELECT_ROLE)
    u.select_role()
    u.fill(u.ADD_USER_MANUALLY_FIRST_NAME, first_name)
    u.fill(u.ADD_USER_MANUALLY_LAST_NAME, last_name)
    u.fill(u.ADD_USER_MANUALLY_MOB_NO, "2025550123")
    u.select_country()
    u.fill(u.ADD_USER_MANUALLY_EMAIL, email)
    u.do_click(u.ADD_USER_MANUALLY_NEXT_BTN_1)
    u.fill(u.ADD_USER_MANUALLY_COMPANY_NAME, company)
    u.fill(u.ADD_USER_MANUALLY_COMPANY_ADDRESS, company_address)
    u.fill(u.ADD_USER_MANUALLY_COMPANY_WEBSITE, company_website)
    u.do_click(u.ADD_USER_MANUALLY_NEXT_BTN_2)
    u.do_click(u.ADD_USER_MANUALLY_ADD_USER_BTN)
    assert u.element_displayed(u.USER_ADDED_SUCCESSFULLY_TEXT), "User added successfully text not displayed"
    logger.info("Test completed successfully: test_add_user_manually")

def _invite_users(driver):
    first_name = faker.first_name()
    last_name = faker.last_name()
    company = faker.company()
    company_address = faker.address()
    company_website = faker.url()
    temp_mail_helper = TempMailHelper()
    email_address = temp_mail_helper.create_email_account()
    logger.info("Starting test: test_invite_users")
    lp = LoginPage(driver)
    db = DashBoard(driver)
    u = User(driver)
    logger.info("Step 1: Performing login")
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    logger.info("Step 2: Verifying dashboard is displayed")
    db.element_displayed(db.DASHBOARD_TEXT)
    db.do_click(db.USER_TAB)
    u.do_click(u.INVITE_USER_BUTTON)
    u.fill(u.INVITE_USER_EMAIL, email_address)
    u.do_click(u.ADD_USER_MANUALLY_SELECT_ROLE)
    u.select_role()
    #time.sleep(5)
    u.do_click(u.INVITE_USER_SEND_INVITE_BUTTON)
    token = temp_mail_helper.wait_for_email()
    logger.info(f"Token:{token}")
    response_register = requests.get(f"https://devadmin.teldrip.com/api/register?token={token}")
    logger.info(f"Response:{response_register.json()}")
    id = response_register.json()["id"]
    logger.info(f"ID:{id}")
    assert response_register.status_code == 200, "Failed to register user"
    payload_set_new_password = {
    "email": email_address,
    "password": "Test@123",
    "token": token
}
    response_set_new_password = requests.post("https://devadmin.teldrip.com/api/set-new-password", json=payload_set_new_password)
    assert response_set_new_password.status_code == 200, "Failed to set new password"
    payload_signupform = {
    "id": id,
    "email": email_address,
    "first_name": first_name,
    "last_name": last_name,
    "phone_no": "+12025550123",
    "terms_and_conditions": True,
    "company": {
        "name": company,
        "website": company_website,
        "address": company_address,
        "company_size": None,
        "timezone": "UTC",
        "industry": None
    }
}

    response_signupform = requests.post("https://devadmin.teldrip.com/api/signupform", json=payload_signupform)
    assert response_signupform.status_code == 201, "Failed to signup form"
    logger.info("Test completed successfully: test_invite_users")