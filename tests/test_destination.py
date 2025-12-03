import time
from constants.constants import Constant
from pages.advertiser_destination_page import AdvertiserDestination
from pages.dashboard_page import DashBoard
from pages.login_page import LoginPage
from utils.logger import Logger

# Initialize logger
logger = Logger.get_logger(__name__)

def test_visibility_of_destination_table(driver):
    logger.info("Starting test: test_visibility_of_destination_table")
    lp = LoginPage(driver)
    
    logger.info("Step 1: Performing login")
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    
    logger.info("Step 2: Verifying dashboard is displayed")
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    
    logger.info("Step 3: Navigating to Advertiser section")
    db.click_advertiser_ele()
    
    logger.info("Step 4: Verifying destination table data is present")
    d = AdvertiserDestination(driver)
    #time.sleep(4)
    assert isinstance(d.is_table_data_present(), str),"Table data not present"
    logger.info("Test completed successfully: test_visibility_of_destination_table")