import time
from constants.constants import Constant
from pages.advertiser_page import Advertiser
from pages.dashboard_page import DashBoard
from pages.login_page import LoginPage
from utils.logger import Logger

# Initialize logger
logger = Logger.get_logger(__name__)

def test_visibility_of_advertiser_table(driver):
    logger.info("Starting test: test_visibility_of_advertiser_table")
    lp = LoginPage(driver)
    
    logger.info("Step 1: Performing login")
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    
    logger.info("Step 2: Verifying dashboard is displayed")
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    
    logger.info("Step 3: Navigating to Advertiser section")
    db.click_advertiser_ele()
    db.do_click(db.ADVERTISER_PAGE_TAB)
    
    logger.info("Step 4: Verifying advertiser table data is present")
    a = Advertiser(driver)
    #time.sleep(4)
    assert isinstance(a.is_table_data_present(), str),"Table data not present"
    logger.info("Test completed successfully: test_visibility_of_advertiser_table")