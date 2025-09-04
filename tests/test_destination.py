import time
from constants.constants import Constant
from pages.advertiser_destination_page import AdvertiserDestination
from pages.dashboard_page import DashBoard
from pages.login_page import LoginPage

def test_visibility_of_destination_table(driver):
    lp = LoginPage(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    db.click_advertiser_ele()
    d = AdvertiserDestination(driver)
    time.sleep(4)
    assert d.is_destination_table_visible()