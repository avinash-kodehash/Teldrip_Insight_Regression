import requests
from constants.constants import Constant
from utils.logger import Logger

# Initialize logger
logger = Logger.get_logger(__name__)

def test_apis_dashboard():
    logger.info("Starting test: test_apis_dashboard")
    
    from pages import base_page
    logger.info("Step 1: Generating authentication token")
    token = base_page.generate_token()
    
    dashboard_endpoints = ["api/updateTimeZone/?user=79",
                           "api/admin-profile/?user=79",
                           "offer/select-plan/?user=79&record=last",
                           "advertiser/country",
                           "api/user-status/?user=79",
                           "api/get-admin-status?user_id=79",
                           "advertiser/time-zone",
                           "api/get-all-profiles"]
    
    logger.info(f"Step 2: Testing {len(dashboard_endpoints)} dashboard API endpoints")
    for index, endpoint in enumerate(dashboard_endpoints, 1):
        url = Constant.BASE_API_URL + endpoint
        headers = {"Authorization": f"Bearer {token}"}
        
        logger.info(f"Testing endpoint {index}/{len(dashboard_endpoints)}: GET {endpoint}")
        response = requests.get(url, headers=headers, timeout=8)
        
        assert response.status_code == 200, f"API {endpoint} failed with status code {response.status_code}"
        logger.info(f"✓ Endpoint passed: {endpoint} (Status: {response.status_code})")
    
    logger.info("Test completed successfully: test_apis_dashboard")