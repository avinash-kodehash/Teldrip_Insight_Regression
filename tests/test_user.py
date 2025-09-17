from constants.constants import Constant
from pages.dashboard_page import DashBoard
from pages.login_page import LoginPage
from pages.user_page import User


def _user_table_visibility(driver):
    lp = LoginPage(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    db.click_advertiser_ele()
    db.do_click(db.USER_TAB)
    u = User(driver)
    #time.sleep(4)
    assert isinstance(u.is_table_data_present(), str),"Table data not present"