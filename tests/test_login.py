from constants.constants import Constant
from pages.dashboard_page import DashBoard
from pages.login_page import LoginPage


def test_login(driver):
    lp = LoginPage(driver)
    db = DashBoard(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db.element_displayed(db.DASHBOARD_TEXT)