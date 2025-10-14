from constants.constants import Constant
from pages.dashboard_page import DashBoard
from pages.login_page import LoginPage
from pages.profile_page import Profile

def test_profile_page_load(driver):
    lp = LoginPage(driver)
    db = DashBoard(driver)
    p = Profile(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db.element_displayed(db.DASHBOARD_TEXT)
    p.do_click(p.PROFILE_BTN)
    p.do_click(p.PROFILE_SUB_BTN)
    assert p.get_element_text(p.PROFILE_NAME) == "Name"
    assert p.get_element_text(p.PROFILE_EMAIL) == "Email ID"
    assert p.get_element_text(p.PROFILE_MOBILE) == "Mobile"
    assert p.get_element_text(p.PROFILE_OFFICE_ADDRESS) == "Office Address"
    assert p.get_element_text(p.PROFILE_BILLING_ADDRESS) == "Billing Address"
    assert p.get_element_text(p.PROFILE_COMPANY_NAME) == "Company Name"

def _page_edit_button(driver):
    lp = LoginPage(driver)
    db = DashBoard(driver)
    p = Profile(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db.element_displayed(db.DASHBOARD_TEXT)
    p.do_click(p.PROFILE_BTN)
    p.do_click(p.PROFILE_SUB_BTN)
    p.do_click(p.PROFILE_EDIT_BUTTON)
    assert p.element_displayed(p.VERIFY_BTN)

def test_profile_edit_invalid_email_format(driver):
    pass

def test_profile_edit_empty_mandatory_fields(driver):
    pass

def test_profile_edit_invalid_phone_no(driver):
    pass

def test_verify_redirect_to_upgrade_plan_page(driver):
    lp = LoginPage(driver)
    db = DashBoard(driver)
    p = Profile(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db.element_displayed(db.DASHBOARD_TEXT)
    p.do_click(p.PROFILE_BTN)
    p.do_click(p.PROFILE_SUB_BTN)
    p.do_click(p.UPGRADE_PLAN_BTN)
    assert p.element_displayed(p.UPGRADE_PLAN_TEXT)