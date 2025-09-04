import time
from constants.constants import Constant
from pages.dashboard_page import DashBoard
from pages.login_page import LoginPage
from pages.offer_page import Offer

def _user_table_visibility(driver):
    lp = LoginPage(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    db.click_advertiser_ele()
    db.do_click(db.USER_TAB)
    o = Offer(driver)
    time.sleep(4)
    assert o.is_offer_table_visible()