import csv
import pytest
from constants.constants import Constant
from pages.dashboard_page import DashBoard
from pages.login_page import LoginPage

def test_login(driver):
    lp = LoginPage(driver)
    db = DashBoard(driver)
    lp.do_login(Constant.Dev_username, Constant.PASSWORD,Constant.otp)
    db.element_displayed(db.DASHBOARD_TEXT)

def read_login_data():
    with open('testdata/invalid_logindata.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [(row['username'], row['password']) for row in reader]

@pytest.mark.parametrize("username,password", read_login_data())
def test_invalid_login_data_driven(driver, username, password):
    lp = LoginPage(driver)
    lp.do_login(username, password)
    assert not lp.is_login_successful()
    #assert lp.element_displayed(lp.EMPTY_EMAIL_ERR_MSG)


