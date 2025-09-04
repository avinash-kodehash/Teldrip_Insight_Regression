import os
import re
import time
import pandas as pd
import requests
from selenium.common import TimeoutException
from constants.constants import Constant
from pages import base_page
from pages.dashboard_page import DashBoard
from pages.login_page import LoginPage
from pages.reporting_page import Reporting

def test_call_details(driver):
    lp = LoginPage(driver)
    r = Reporting(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    db.click_reporting_ele()
    r.set_date()
    r.do_click(r.CALL_DETAILS_TAB)
    time.sleep(5)
    r.is_call_details_tab_data_present()

def test_campaign_table(driver):
    lp = LoginPage(driver)
    r = Reporting(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    db.click_reporting_ele()
    r.set_date()
    r.do_click(r.CAMPAIGN_TAB)
    time.sleep(5)
    r.element_displayed(r.DATA)

def test_publisher_table(driver):
    lp = LoginPage(driver)
    r = Reporting(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    db.click_reporting_ele()
    r.set_date()
    r.do_click(r.PUBLISHER_TAB)
    time.sleep(5)
    r.element_displayed(r.DATA)

def test_advertiser_table(driver):
    lp = LoginPage(driver)
    r = Reporting(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    db.click_reporting_ele()
    r.set_date()
    r.do_click(r.ADVERTISER_TAB)
    time.sleep(5)
    r.element_displayed(r.DATA)

def test_destination_table(driver):
    lp = LoginPage(driver)
    r = Reporting(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    db.click_reporting_ele()
    r.set_date()
    r.do_click(r.DESTINATION_TAB)
    time.sleep(5)
    r.element_displayed(r.DATA)

def test_caller_id_table(driver):
    lp = LoginPage(driver)
    r = Reporting(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    db.click_reporting_ele()
    r.set_date()
    r.do_click(r.CALLER_ID_TAB)
    time.sleep(5)
    r.element_displayed(r.DATA)

def test_dialled_no_table(driver):
    lp = LoginPage(driver)
    r = Reporting(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    db.click_reporting_ele()
    r.set_date()
    r.do_click(r.DIALLED_NO_TAB)
    time.sleep(5)
    r.element_displayed(r.DATA)

def test_data_in_call_volume_trend_chart(driver):
    lp = LoginPage(driver)
    r = Reporting(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    db.click_reporting_ele()
    r.set_date()
    time.sleep(2)
    r.do_click(r.REFRESH_BUTTON)
    try:
        r.element_displayed(r.CONNECTED_CALLS)
    except TimeoutException:
        print("Call trend chart is not displayed")
    r.get_call_values_as_list([
        r.INCOMING_CALLS,
        r.CONNECTED_CALLS,
        r.NOT_CONNECTED_CALLS,
        r.CONVERTED_CALLS,
        r.HANGUP_CALLS,
    ])
    for n in r.num:
        assert n>0,f"the value:{n} is not greater than 0"

def test_call_status_overview_chart(driver):
    lp = LoginPage(driver)
    r = Reporting(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    db.click_reporting_ele()
    r.set_date()
    time.sleep(2)
    r.do_click(r.REFRESH_BUTTON)
    try:
        r.element_displayed(r.CSO_INCOMING_CALLS)
    except TimeoutException:
        print("Call status overview chart is not displayed")

    time.sleep(3)
    r.scroll_to_element(r.CONNECTED_CALLS)
    time.sleep(3)
    assert int(r.get_element_text(r.CSO_COMPLETED_CALLS))>0,"Completed calls value is not greater than 0"
    assert int(r.get_element_text(r.CSO_CONNECTED_CALLS))>0,"Connected calls value is not greater than 0"
    assert int(r.get_element_text(r.CSO_CONVERTED_CALLS))>0,"Converted calls value is not greater than 0"
    assert int(r.get_element_text(r.CSO_DUPLICATE_CALLS))>0,"Duplicate calls value is not greater than 0"
    assert int(r.get_element_text(r.CSO_INCOMING_CALLS))>0,"Incoming calls value is not greater than 0"


def test_compare_values_trend_chart_and_overview_chart(driver):
    lp = LoginPage(driver)
    r = Reporting(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    db.click_reporting_ele()
    r.set_date()
    time.sleep(2)
    r.do_click(r.REFRESH_BUTTON)
    try:
        r.element_displayed(r.CONNECTED_CALLS)
    except TimeoutException:
        print("Call trend chart is not displayed")

    r.get_call_values_as_list([
        r.INCOMING_CALLS,
        r.CONNECTED_CALLS,
        r.CONVERTED_CALLS,
    ])
    r.scroll_to_element(r.CONNECTED_CALLS)
    time.sleep(3)
    cso_connected = int(r.get_element_text(r.CSO_CONNECTED_CALLS))
    cso_converted = int(r.get_element_text(r.CSO_CONVERTED_CALLS))
    cso_incoming = int(r.get_element_text(r.CSO_INCOMING_CALLS))
    l = [cso_incoming ,cso_connected, cso_converted]
    assert r.num == l, f"Expected {l}, but got {r.num}"

def test_compare_values_trend_chart_and_dropped_calls_chart(driver):
    lp = LoginPage(driver)
    r = Reporting(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    db.click_reporting_ele()
    r.set_date()
    time.sleep(2)
    r.do_click(r.REFRESH_BUTTON)
    try:
        r.element_displayed(r.CONNECTED_CALLS)
    except TimeoutException:
        print("Call trend chart is not displayed")

    r.get_call_values_as_list([
        r.NOT_CONNECTED_CALLS,
        r.HANGUP_CALLS,
        r.BLOCKED_CALLS,
    ])
    r.scroll_to_element(r.CONNECTED_CALLS)
    time.sleep(3)
    cd_not_connected = int(r.get_element_text(r.CD_NOT_CONNECTED_CALLS))
    cd_hangup = int(r.get_element_text(r.CD_HANGUP_CALLS))
    cd_blocked = int(r.get_element_text(r.CD_BLOCKED_CALLS))
    l = [cd_not_connected, cd_hangup, cd_blocked]
    assert r.num == l, f"Expected {l}, but got {r.num}"

def test_total_calls(driver):
    lp = LoginPage(driver)
    r = Reporting(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    db.click_reporting_ele()
    r.set_date()
    time.sleep(2)
    r.do_click(r.REFRESH_BUTTON)
    assert r.element_displayed(r.TOTAL_CALLS)
    act_total_calls = int(r.get_element_text(r.TOTAL_CALLS))
    incoming_calls = int(r.get_element_text(r.CSO_INCOMING_CALLS))
    sys_hangup_calls = int(r.get_element_text(r.CD_SYS_HANGUP_CALLS))
    exp_total_calls = incoming_calls + sys_hangup_calls
    assert act_total_calls == exp_total_calls, f"Expected total calls: {exp_total_calls}, but got {act_total_calls}"

def test_gross_profit(driver):
    lp = LoginPage(driver)
    r = Reporting(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    db.click_reporting_ele()
    r.set_date()
    time.sleep(2)
    r.do_click(r.REFRESH_BUTTON)
    act_gross_profit = float(r.get_element_text(r.GROSS_PROFIT).replace("$", ""))
    exp_gross_profit = float(r.get_element_text(r.REVENUE).replace("$", "")) - float(r.get_element_text(r.PAYOUT).replace("$", ""))
    assert act_gross_profit == exp_gross_profit

def test_net_profit(driver):
    lp = LoginPage(driver)
    r = Reporting(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    db.click_reporting_ele()
    r.set_date()
    time.sleep(2)
    r.do_click(r.REFRESH_BUTTON)
    act_net_profit = float(r.get_element_text(r.NET_PROFIT).replace("$", ""))
    exp_net_profit = float(r.get_element_text(r.REVENUE).replace("$", "")) - float(r.get_element_text(r.EXPENSE).replace("$", ""))
    assert act_net_profit == exp_net_profit, f"Expected net profit: {exp_net_profit}, but got {act_net_profit}"

def normalize_value(val):
    if isinstance(val, str):
        # Remove all spaces and plus signs
        return re.sub(r'[\s+]', '', val)
    return val

def test_reporting_export_this_page(driver_with_downloads):
    driver = driver_with_downloads
    lp = LoginPage(driver)
    r = Reporting(driver)
    lp.do_login(Constant.USERNAME, Constant.PASSWORD)
    db = DashBoard(driver)
    db.element_displayed(db.DASHBOARD_TEXT)
    db.click_reporting_ele()
    r.set_date()
    time.sleep(2)
    r.do_click(r.REFRESH_BUTTON)
    time.sleep(3)
    r.scroll_to_element(r.CALL_DETAILS_TAB)
    r.wait_for_table_to_load(r.FIRST_CELL)
    r.select_table_dropdown("100")
    r.wait_for_table_to_load(r.FIRST_CELL)
    r.scroll_to_element(r.TOTAL_CALLS)
    r.do_click(r.EXPORT_BUTTON)
    r.do_click(r.EXPORT_SUB_BUTTON)
    time.sleep(2)
    files = [f for f in os.listdir(driver.download_dir) if f.endswith(".csv")]
    assert files, "No CSV file found!"
    csv_file_path = os.path.join(driver.download_dir, files[0])
    # read downloaded csv
    csv_data = pd.read_csv(csv_file_path, sep=",", engine="python")
    # get UI dataframe
    ui_df = r.get_table_as_dataframe()
    # save UI data for debugging/reference
    ui_df.to_csv("ui_data.csv", index=False)
    ui_csv = pd.read_csv("ui_data.csv")
    # Strip column names
    csv_data.columns = [col.strip() for col in csv_data.columns]
    ui_csv.columns = [col.strip() for col in ui_csv.columns]
    #csv_data = csv_data[ui_df.columns]
    csv_data = csv_data.astype(str)
    ui_csv = ui_csv.astype(str)
    csv_data = csv_data.applymap(normalize_value)
    ui_csv = ui_csv.applymap(normalize_value)
    # compare
    pd.testing.assert_frame_equal(csv_data, ui_csv, check_dtype=False)


def test_reporting_get_apis():
    token = base_page.generate_token()
    reporting_endpoints = ["offer/select-plan/?user=79&record=last",
                           "api/updateTimeZone/?user=79",
                           "api/get-admin-status?user_id=79",
                           "api/user-status/?user=79",
                           "advertiser/time-zone",
                           "advertiser/country",
                           "api/get-all-profiles",
                           "api/admin-profile/?user=79",
                           "campaign/reports/export-report-data"
                          ]
    for endpoint in reporting_endpoints:
        url = Constant.BASE_API_URL + endpoint
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(url, headers=headers, timeout=8)
        assert response.status_code == 200, f"API {endpoint} failed with status code {response.status_code}"

def test_reporting_post_apis():
    token = base_page.generate_token()
    reporting_post_endpoints = [
        {
            "endpoint": "campaign/reports/all-call-details",
            "payload": {"fromDate":"2025-08-30","toDate":"2025-08-30","type_of_user":"admin","time_zone":"America/New_York","user_id":79,"filters":{}}
        },
        {
            "endpoint": "campaign/reports/calls-as-per-campaign",
            "payload": {"fromDate":"2025-08-30","toDate":"2025-08-30","type_of_user":"admin","time_zone":"America/New_York","user_id":79,"filters":{}}
        },
        {
            "endpoint": "campaign/dashboard/revenue-payout",
            "payload": {"custom_start":"2025-08-30","custom_end":"2025-08-30","frequency":"custom","type_of_user":"admin","time_zone":"America/New_York","user_id":79,"filters":{}}
        },
        {
            "endpoint": "campaign/reports/each-call-details?page=1&page_count=10",
            "payload": {"fromDate":"2025-08-30","toDate":"2025-08-30","type_of_user":"admin","type":"call_details","search":"","filters":{},"user_id":79,"time_zone":"America/New_York","specific_filters":{"category":"call_details"}}
        },
        {
            "endpoint": "campaign/reports/insights?page=1&page_count=10",
            "payload": {"fromDate":"2025-08-29","toDate":"2025-08-29","type_of_user":"admin","type":"campaign","search":"","filters":{},"user_id":79,"time_zone":"America/New_York","specific_filters":{"category":"campaign"}}
        },
        {
            "endpoint": "campaign/reports/insights?page=1&page_count=10",
            "payload" : {"fromDate":"2025-08-29","toDate":"2025-08-29","type_of_user":"admin","type":"publisher","search":"","user_id":79,"time_zone":"America/New_York","filters":{},"specific_filters":{"category":"publisher"}}
        },
        {
            "endpoint": "campaign/reports/insights?page=1&page_count=10",
            "payload": {"fromDate":"2025-08-29","toDate":"2025-08-29","type_of_user":"admin","type":"advertiser","search":"","user_id":79,"time_zone":"America/New_York","filters":{},"specific_filters":{"category":"advertiser"}}
        },
        {
            "endpoint": "campaign/reports/insights?page=1&page_count=10",
            "payload": {"fromDate":"2025-08-29","toDate":"2025-08-29","type_of_user":"admin","type":"destination","search":"","user_id":79,"time_zone":"America/New_York","filters":{},"specific_filters":{"category":"destination"}}
        },
        {
            "endpoint": "campaign/reports/insights?page=1&page_count=10",
            "payload": {"fromDate":"2025-08-29","toDate":"2025-08-29","type_of_user":"admin","type":"callers","search":"","user_id":79,"time_zone":"America/New_York","filters":{},"specific_filters":{"category":"callers"}}
        },
        {
            "endpoint": "campaign/reports/insights?page=1&page_count=10",
            "payload": {"fromDate":"2025-08-29","toDate":"2025-08-29","type_of_user":"admin","type":"dialed_numbers","search":"","user_id":79,"time_zone":"America/New_York","filters":{},"specific_filters":{"category":"dialed_numbers"}}
        },
        {
            "endpoint": "campaign/reports/each-call-details?paginate=false",
            "payload": {"fromDate": "2025-07-01", "toDate": "2025-07-31", "type_of_user": "admin",
                        "type": "call_details", "search": "", "filters": {}, "user_id": 79,
                        "time_zone": "America/New_York", "specific_filters": {"category": "call_details"},
                        "file_type": "CSV"}
        }
    ]

    for api in reporting_post_endpoints:
        url = Constant.BASE_API_URL + api["endpoint"]
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        response = requests.post(url, headers=headers, json=api["payload"], timeout=8)
        assert response.status_code == 200,f"POST API {api['endpoint']} failed with status code {response.status_code}"
