from constants.constants import Constant
from pages.dashboard_page import DashBoard
from pages.login_page import LoginPage
from pages.profile_page import Profile
from utils.logger import Logger

# Initialize logger
logger = Logger.get_logger(__name__)

def test_profile_page_load(driver):
    logger.info("Starting test: test_profile_page_load")
    lp = LoginPage(driver)
    db = DashBoard(driver)
    p = Profile(driver)
    
    logger.info("Step 1: Performing login")
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    
    logger.info("Step 2: Verifying dashboard is displayed")
    db.element_displayed(db.DASHBOARD_TEXT)
    
    logger.info("Step 3: Navigating to Profile page")
    p.do_click(p.PROFILE_BTN)
    p.do_click(p.PROFILE_SUB_BTN)
    
    logger.info("Step 4: Verifying profile fields are displayed correctly")
    assert p.get_element_text(p.PROFILE_NAME) == "Name"
    assert p.get_element_text(p.PROFILE_EMAIL) == "Email ID"
    assert p.get_element_text(p.PROFILE_MOBILE) == "Mobile"
    assert p.get_element_text(p.PROFILE_OFFICE_ADDRESS) == "Office Address"
    assert p.get_element_text(p.PROFILE_BILLING_ADDRESS) == "Billing Address"
    assert p.get_element_text(p.PROFILE_COMPANY_NAME) == "Company Name"
    logger.info("Test completed successfully: test_profile_page_load")

def _page_edit_button(driver):
    lp = LoginPage(driver)
    db = DashBoard(driver)
    p = Profile(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db.element_displayed(db.DASHBOARD_TEXT)
    p.do_click(p.PROFILE_BTN)
    p.do_click(p.PROFILE_SUB_BTN)
    p.do_click(p.PROFILE_EDIT_BUTTON)
    assert p.element_displayed(p.VERIFY_BTN)

def test_profile_edit_invalid_email_format(driver):
    pass

def test_profile_edit_empty_mandatory_fields(driver):
    pass

def test_profile_edit_invalid_phone_no(driver):
    pass

def test_verify_redirect_to_upgrade_plan_page(driver):
    logger.info("Starting test: test_verify_redirect_to_upgrade_plan_page")
    lp = LoginPage(driver)
    db = DashBoard(driver)
    p = Profile(driver)
    
    logger.info("Step 1: Performing login")
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    
    logger.info("Step 2: Verifying dashboard is displayed")
    db.element_displayed(db.DASHBOARD_TEXT)
    
    logger.info("Step 3: Navigating to Profile page")
    p.do_click(p.PROFILE_BTN)
    p.do_click(p.PROFILE_SUB_BTN)
    
    logger.info("Step 4: Clicking Upgrade Plan button")
    p.do_click(p.UPGRADE_PLAN_BTN)
    
    logger.info("Step 5: Verifying upgrade plan page is displayed")
    assert p.element_displayed(p.UPGRADE_PLAN_TEXT)
    logger.info("Test completed successfully: test_verify_redirect_to_upgrade_plan_page")