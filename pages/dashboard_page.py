from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashBoard(BasePage):

    REPORTING_ELE = (By.XPATH,"(//*[name()='svg'])[3]")
    DASHBOARD_TEXT = (By.XPATH,"//h1[normalize-space()='Dashboard']")
    LOGOUT_BUTTON = (By.CSS_SELECTOR,"div[class='menu-bottom-list-item MuiBox-root css-1jyjgz'] svg")
    LOGOUT_YES_BUTTON = (By.XPATH,"//button[normalize-space()='Yes']")
    ADVERTISER_TAB = (By.XPATH,"(//*[name()='svg'])[6]")
    ADVERTISER_PAGE_TAB = (By.XPATH, "(//div[contains(@class,'MuiListItemText-root css-1tsvksn')])[7]")
    ADVERTISER_TABLE = (By.CSS_SELECTOR,".text-sm.text-primary-500")
    OFFER_TAB = (By.XPATH, "(//*[name()='svg'])[6]")
    USER_TAB = (By.XPATH, "(//*[name()='svg'])[8]")
    FIRST_CELL = (By.XPATH, "//tr[1]//td[2]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_reporting_ele(self):
        self.do_click(self.REPORTING_ELE)

    def click_advertiser_ele(self):
        self.do_click(self.ADVERTISER_TAB)

    def is_table_data_present(self):
        self.wait_for_non_empty_text(self.FIRST_CELL)
        return self.driver.find_element(*self.FIRST_CELL).text


