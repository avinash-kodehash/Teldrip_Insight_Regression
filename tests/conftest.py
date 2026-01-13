import os
import shutil
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from constants.constants import Constant
from utils.logger import Logger

# Initialize logger for conftest
logger = Logger.get_logger("ConfTest")

@pytest.fixture(scope="function")
def driver(request):
    """WebDriver fixture with logging support"""
    test_name = request.node.name
    logger.info(f"Setting up WebDriver for test: {test_name}")
    
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Constant.BASE_URL)
    logger.info(f"WebDriver initialized successfully for test: {test_name}")
    logger.info(f"Navigated to URL: {Constant.BASE_URL}")
    
    yield driver
    
    logger.info(f"Tearing down WebDriver for test: {test_name}")
    driver.quit()
    logger.info(f"WebDriver closed successfully for test: {test_name}")

@pytest.fixture(scope="function")
def driver_with_downloads(request):
    """WebDriver fixture with download support and logging"""
    test_name = request.node.name
    logger.info(f"Setting up WebDriver with downloads for test: {test_name}")
    
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    download_dir = os.path.join(project_root, "downloaded_csv")

    if os.path.exists(download_dir):
        shutil.rmtree(download_dir)
        logger.debug(f"Cleaned up existing download directory: {download_dir}")
    
    os.makedirs(download_dir)
    logger.info(f"Created download directory: {download_dir}")
    
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.get(Constant.BASE_URL)
    driver.maximize_window()
    driver.download_dir = download_dir
    
    logger.info(f"WebDriver with downloads initialized successfully for test: {test_name}")
    
    yield driver  # hand control to test
    
    logger.info(f"Tearing down WebDriver with downloads for test: {test_name}")
    driver.quit()
    if os.path.exists(download_dir):
        shutil.rmtree(download_dir)
        logger.debug(f"Cleaned up download directory: {download_dir}")

# Pytest Hooks for Logging Integration

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """
    Called before test session starts
    Clean up old logs and setup logging
    """
    logger.info("=" * 100)
    logger.info("TEST SESSION STARTING")
    logger.info(f"Session started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("=" * 100)
    
    # Clean up old log files (keep last 7 days)
    Logger.cleanup_old_logs(days=7)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_setup(item):
    """Called before each test setup"""
    test_name = item.nodeid
    logger.info("")
    logger.info("=" * 100)
    logger.info(f"SETTING UP TEST: {test_name}")
    logger.info("=" * 100)
    yield


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item):
    """Called during test execution"""
    test_name = item.nodeid
    logger.info(f"EXECUTING TEST: {test_name}")
    yield


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_teardown(item):
    """Called after each test teardown"""
    test_name = item.nodeid
    logger.info(f"TEARING DOWN TEST: {test_name}")
    logger.info("=" * 100)
    yield


def pytest_runtest_makereport(item, call):
    """
    Called after each test phase (setup, call, teardown)
    Log test results
    """
    if call.when == "call":
        test_name = item.nodeid
        if call.excinfo is not None:
            logger.error(f"TEST FAILED: {test_name}")
            logger.error(f"Error: {call.excinfo.value}")
        else:
            logger.info(f"TEST PASSED: {test_name}")


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    """
    Called after test session finishes
    Log session summary
    """
    logger.info("")
    logger.info("=" * 100)
    logger.info("TEST SESSION FINISHED")
    logger.info(f"Session ended at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info(f"Exit status: {exitstatus}")
    
    # Log test statistics
    if hasattr(session, 'testscollected'):
        logger.info(f"Total tests collected: {session.testscollected}")
    if hasattr(session, 'testsfailed'):
        logger.info(f"Total tests failed: {session.testsfailed}")
    
    logger.info("=" * 100)
    
    # Original allure report generation code (commented)
    # results_dir = "reports/allure-results"
    # report_dir = "reports/allure-report"
    #
    # if os.path.exists(results_dir) and os.listdir(results_dir):
    #     try:
    #         subprocess.run(
    #             ["allure", "generate", results_dir, "-o", report_dir, "--clean"],
    #             check=True
    #         )
    #         print(f"\n✅ Allure report generated at: {os.path.abspath(report_dir)}\n")
    #     except Exception as e:
    #         print(f"\n❌ Failed to generate Allure report: {e}\n")
    # else:
    #     print("\n⚠️ No Allure results found. Did you run pytest with allure-pytest enabled?\n")
