import requests
from constants.constants import Constant

def test_apis_dashboard():
    from pages import base_page
    token = base_page.generate_token()
    dashboard_endpoints = ["api/updateTimeZone/?user=79",
                           "api/admin-profile/?user=79",
                           "offer/select-plan/?user=79&record=last",
                           "advertiser/country",
                           "api/user-status/?user=79",
                           "api/get-admin-status?user_id=79",
                           "advertiser/time-zone",
                           "api/get-all-profiles"]
    for endpoint in dashboard_endpoints:
        url = Constant.BASE_API_URL + endpoint
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(url, headers=headers, timeout=8)
        assert response.status_code == 200, f"API {endpoint} failed with status code {response.status_code}"
        #print(response.status_code)