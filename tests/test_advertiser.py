import time
from constants.constants import Constant
from pages.advertiser_page import Advertiser
from pages.dashboard_page import DashBoard
from pages.login_page import LoginPage

def test_visibility_of_advertiser_table(driver):
    lp = LoginPage(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    db.click_advertiser_ele()
    db.do_click(db.ADVERTISER_PAGE_TAB)
    a = Advertiser(driver)
    #time.sleep(4)
    assert isinstance(a.is_table_data_present(), str),"Table data not present"