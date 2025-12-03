import csv
import pytest
from constants.constants import Constant
from pages.dashboard_page import DashBoard
from pages.login_page import LoginPage
from utils.logger import Logger

# Initialize logger
logger = Logger.get_logger(__name__)

def test_login(driver):
    logger.info("Starting test: test_login")
    lp = LoginPage(driver)
    db = DashBoard(driver)
    
    logger.info("Step 1: Performing login with valid credentials")
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    
    logger.info("Step 2: Verifying dashboard is displayed")
    db.element_displayed(db.DASHBOARD_TEXT)
    logger.info("Test completed successfully: test_login")

def read_login_data():
    with open('testdata/invalid_logindata.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [(row['username'], row['password']) for row in reader]

@pytest.mark.parametrize("username,password", read_login_data())
def test_invalid_login_data_driven(driver, username, password):
    logger.info(f"Starting test: test_invalid_login_data_driven with username={username}")
    lp = LoginPage(driver)
    
    logger.info("Step 1: Attempting login with invalid credentials")
    lp.do_login(username, password)
    
    logger.info("Step 2: Verifying login failed as expected")
    assert not lp.is_login_successful()
    logger.info("Test completed successfully: Invalid login rejected as expected")
    #assert lp.element_displayed(lp.EMPTY_EMAIL_ERR_MSG)


