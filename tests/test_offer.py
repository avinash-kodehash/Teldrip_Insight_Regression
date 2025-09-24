import time
from constants.constants import Constant
from pages.dashboard_page import DashBoard
from pages.login_page import LoginPage
from pages.offer_page import Offer
from datetime import datetime

def test_offer_page_title(driver):
    lp = LoginPage(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    db.click_offer_ele()
    #db.do_click(db.OFFER_TAB)
    o = Offer(driver)
    assert o.get_element_text(o.OFFER_TITLE) == "Offer", "Offer page title mismatch"

def test_offer_table_visibility(driver):
    lp = LoginPage(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    db.click_offer_ele()
    #db.do_click(db.OFFER_TAB)
    o = Offer(driver)
    assert isinstance(o.is_table_data_present(), str),"Table data not present"

def test_offer_table_date_format(driver):
    lp = LoginPage(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    db.click_offer_ele()
    # db.do_click(db.OFFER_TAB)
    o = Offer(driver)
    assert isinstance(o.is_table_data_present(), str), "Table data not present"
    act_start_date = o.get_element_text(o.TABLE_START_DATE)
    #act_end_date = o.get_element_text(o.TABLE_END_DATE)
    assert datetime.strptime(act_start_date, "%m/%d/%Y")
    #assert datetime.strptime(act_end_date, "%m/%d/%Y")

def test_offer_search_functionality(driver):
    lp = LoginPage(driver)
    o = Offer(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    db.click_offer_ele()
    # db.do_click(db.OFFER_TAB)
    assert isinstance(o.is_table_data_present(), str), "Table data not present"
    #o.do_click(o.SEARCH_INPUT)
    o.select_table_count("100")
    assert isinstance(o.is_table_data_present(), str), "Table data not present"
    o.fill(o.SEARCH_INPUT, Constant.OFFER_SEARCH)
    time.sleep(4)
    offer_name_list = o.get_offer_name_list()
    for name in offer_name_list:
        assert Constant.OFFER_SEARCH in name.lower(), f"Search functionality not working, {name} does not contain 'avi'"

def test_create_new_offer(driver):
    lp = LoginPage(driver)
    o = Offer(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    db.click_offer_ele()
    #assert isinstance(o.is_table_data_present(), str), "Table data not present"
    o.do_click(o.CREATE_OFFER_BUTTON)
    assert o.element_displayed(o.CREATE_OFFER_HEADER)
    o.fill(o.OFFER_NAME_INPUT, Constant.CREATE_OFFER_NAME)
    o.select_country()
    o.select_offer_start_date()
    o.select_offer_end_date()
    o.select_offer_visibility()
    o.select_conversion_type()
    o.select_conversion_method()
    o.select_call_timer_start()
    o.fill(o.DURATION_INPUT, Constant.DURATION_IN_SECONDS)
    o.select_payout_method()
    o.fill(o.PAYOUT_INPUT, Constant.PAYOUT_AMOUNT)
    o.fill(o.REVENUE_INPUT, Constant.PAYOUT_AMOUNT)
    o.select_duplicate_timeframe()
    o.do_click(o.CREATE_OFFER_BTN)
    assert isinstance(o.is_table_data_present(), str), "Table data not present"
    assert o.get_element_text(o.FIRST_OFFER_NAME) == Constant.CREATE_OFFER_NAME, "New offer not created"

def test_req_received_publisher(driver):
    lp = LoginPage(driver)
    o = Offer(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    db.click_offer_ele()
    assert isinstance(o.is_table_data_present(), str), "Table data not present"
    o.select_table_count("100")
    assert isinstance(o.is_table_data_present(), str), "Table data not present"
    req_rec_list = o.get_elements_as_list(o.PUBLISHER_REQUEST_COLUMN)
    for ele in req_rec_list:
        if ele.text != '0':
            ele.click()
            break
    assert isinstance(o.is_table_data_present(), str), "Table data not present"

def test_delete_offer(driver):
    lp = LoginPage(driver)
    o = Offer(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    db.click_offer_ele()
    assert isinstance(o.is_table_data_present(), str), "Table data not present"
    o.do_click(o.DELETE_OFFER_BUTTON)
    o.do_click(o.DELETE_OFFER_YES_BUTTON)
    time.sleep(2)
    text = o.get_element_text(o.POPUP_OFFER_DELETED)
    assert text == "Offer deleted successfully", "Offer not deleted"

def test_edit_offer(driver):
    lp = LoginPage(driver)
    o = Offer(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    db.click_offer_ele()
    assert isinstance(o.is_table_data_present(), str), "Table data not present"
    #o.do_click(o.CREATE_OFFER_BUTTON)
    #assert o.element_displayed(o.CREATE_OFFER_HEADER)
    #time.sleep(5)
    o.do_click(o.EDIT_OFFER_BUTTON)
    #time.sleep(5)
    #assert o.element_displayed(o.CREATE_OFFER_HEADER)
    o.clear_input_field(o.OFFER_NAME_INPUT)
    o.fill(o.OFFER_NAME_INPUT, Constant.EDIT_OFFER_NAME)
    o.edit_country()
    o.edit_offer_start_date()
    o.edit_offer_end_date()
    o.edit_offer_visibility()
    o.edit_conversion_type()
    o.edit_conversion_method()
    o.edit_call_timer_start()
    o.clear_input_field(o.DURATION_INPUT)
    o.fill(o.DURATION_INPUT, Constant.EDIT_DURATION_IN_SECONDS)
    o.edit_payout_method()
    o.clear_input_field(o.PAYOUT_INPUT)
    o.fill(o.PAYOUT_INPUT, Constant.EDIT_PAYOUT_AMOUNT)
    o.clear_input_field(o.REVENUE_INPUT)
    o.fill(o.REVENUE_INPUT, Constant.EDIT_PAYOUT_AMOUNT)
    o.edit_duplicate_timeframe()
    o.do_click(o.UPDATE_OFFER_BTN)
    text = o.get_element_text(o.POPUP_OFFER_UPDATED)
    assert text == "Offer updated successfully", "Offer not updated"

def test_duplicate_offer(driver):
    lp = LoginPage(driver)
    o = Offer(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    db.click_offer_ele()
    assert isinstance(o.is_table_data_present(), str), "Table data not present"
    o.do_click(o.DUPLICATE_OFFER_BUTTON)
    o.do_click(o.DUPLICATE_OFFER_YES_BUTTON)
    o.clear_input_field(o.OFFER_NAME_INPUT)
    o.fill(o.OFFER_NAME_INPUT, Constant.DUP_OFFER_NAME)
    o.do_click(o.UPDATE_OFFER_BTN)
    text = o.get_element_text(o.POPUP_OFFER_UPDATED)
    assert text == "Offer updated successfully", "Offer not updated"

def test_status_button(driver):
    lp = LoginPage(driver)
    o = Offer(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    db.click_offer_ele()
    assert isinstance(o.is_table_data_present(), str), "Table data not present"
    o.do_click(o.STATUS_BUTTON)
    time.sleep(1)
    text = o.get_element_text(o.POPUP_STATUS_BTN)
    assert text == "updated", "Status button not working"

def test_export_offer(driver_with_downloads):
    driver = driver_with_downloads
    lp = LoginPage(driver)
    o = Offer(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    db.click_offer_ele()
    assert isinstance(o.is_table_data_present(), str), "Table data not present"
