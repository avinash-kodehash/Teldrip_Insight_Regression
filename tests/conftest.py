import os
import shutil

import pytest
from selenium import webdriver
from constants.constants import Constant

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get(Constant.BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def driver_with_downloads():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    download_dir = os.path.join(project_root, "downloaded_csv")

    if os.path.exists(download_dir):
        shutil.rmtree(download_dir)
    os.makedirs(download_dir)
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
    yield driver  # hand control to test
    driver.quit()
    if os.path.exists(download_dir):
        shutil.rmtree(download_dir)

# @pytest.hookimpl(tryfirst=True)
# def pytest_sessionfinish(session, exitstatus):
#     results_dir = "reports/allure-results"
#     report_dir = "reports/allure-report"
#
#     if os.path.exists(results_dir) and os.listdir(results_dir):
#         try:
#             subprocess.run(
#                 ["allure", "generate", results_dir, "-o", report_dir, "--clean"],
#                 check=True
#             )
#             print(f"\n✅ Allure report generated at: {os.path.abspath(report_dir)}\n")
#         except Exception as e:
#             print(f"\n❌ Failed to generate Allure report: {e}\n")
#     else:
#         print("\n⚠️ No Allure results found. Did you run pytest with allure-pytest enabled?\n")
