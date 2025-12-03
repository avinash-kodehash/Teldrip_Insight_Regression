from constants.constants import Constant
from pages.dashboard_page import DashBoard
from pages.login_page import LoginPage
from utils.logger import Logger

# Initialize logger
logger = Logger.get_logger(__name__)

def test_logout(driver):
    logger.info("Starting test: test_logout")
    lp = LoginPage(driver)
    db = DashBoard(driver)
    
    logger.info("Step 1: Performing login")
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    
    logger.info("Step 2: Verifying dashboard is displayed")
    db.element_displayed(db.DASHBOARD_TEXT)
    
    logger.info("Step 3: Clicking logout button")
    db.do_click(db.LOGOUT_BUTTON)
    
    logger.info("Step 4: Confirming logout")
    db.do_click(db.LOGOUT_YES_BUTTON)
    
    logger.info("Step 5: Verifying login page elements are displayed")
    lp.element_displayed(lp.EMAIL)
    lp.element_displayed(lp.PASSWORD)
    lp.element_displayed(lp.LOGIN_BUTTON)
    logger.info("Test completed successfully: test_logout")