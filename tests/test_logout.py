from constants.constants import Constant
from pages.dashboard_page import DashBoard
from pages.login_page import LoginPage


def test_logout(driver):
    lp = LoginPage(driver)
    db = DashBoard(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db.element_displayed(db.DASHBOARD_TEXT)
    db.do_click(db.LOGOUT_BUTTON)
    db.do_click(db.LOGOUT_YES_BUTTON)
    lp.element_displayed(lp.EMAIL)
    lp.element_displayed(lp.PASSWORD)
    lp.element_displayed(lp.LOGIN_BUTTON)