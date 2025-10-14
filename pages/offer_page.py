from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import BasePage
from constants.constants import Constant


class Offer(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    CREATE_OFFER_BUTTON = (By.XPATH, "(//*[name()='svg'][@class='inline-block w-5 h-5'])[1]")
    OFFER_NAME_INPUT = (By.XPATH, "//input[@placeholder='Enter Offer Name']")
    OFFER_DESC_INPUT = (By.XPATH, "//span[@class='jodit-placeholder']")
    COUNTRY_DROPDOWN = (By.XPATH, "//input[@placeholder='Select Country']")
    ALL_COUNTRY_OPTION = (By.XPATH, "//li")
    ALL_CONVERSION_DROPDOWN = (By.XPATH, "//li")
    DUPLICATE_TIMEFRAME_ENABLE = (By.XPATH, "//span[normalize-space()='Enable']")
    DUPLICATE_TIMEFRAME_disable = (By.XPATH, "//span[@class='text-sm font-semibold'][normalize-space()='Disable']")
    DUPLICATE_TIMEFRAME_TIMELIMIT = (By.XPATH, "//span[normalize-space()='Time Limit']")
    PAYOUT_INPUT = (By.XPATH, "(//input[@placeholder='Enter Amount'])[1]")
    REVENUE_INPUT = (By.XPATH, "(//input[@placeholder='Enter Amount'])[2]")
    PAYOUT_METHOD_CPL = (By.XPATH, "//span[normalize-space()='CPL']")
    PAYOUT_METHOD_CPA = (By.XPATH, "//span[normalize-space()='CPA']")
    PAYOUT_METHOD_REV_SHARE = (By.XPATH, "//span[normalize-space()='Rev Share']")
    DURATION_INPUT = (By.XPATH, "//input[@placeholder='Enter duration in seconds']")
    CALL_TIMER_START_INCOMING = (By.XPATH, "//span[normalize-space()='Incoming']")
    CALL_TIMER_START_CONNECTED = (By.XPATH, "//span[normalize-space()='Connected']")
    CALL_TIMER_START_DIALLED = (By.XPATH, "//span[normalize-space()='Dialed']")
    CONVERSION_METHOD = (By.XPATH, "//input[@placeholder='Select Conversion Method']")
    CONVERSION_TYPE_DYNAMIC = (By.XPATH, "//span[normalize-space()='Dynamic']")
    CONVERSION_TYPE_STATIC = (By.XPATH, "//span[normalize-space()='Static']")
    OFFER_VISIBILITY_PUBLIC = (By.XPATH, "//span[normalize-space()='Public']")
    OFFER_NAME_COLUMN = "//td[3]/a" # Not using By.XPATH to use in get_elements_text_as_list method
    OFFER_VISIBILITY_PRIVATE = (By.XPATH, "//span[normalize-space()='Private']")
    CREATE_OFFER_HEADER = (By.XPATH, "//span[normalize-space()='Create New Offer']")
    OFFER_START_DATE = (By.XPATH, "//input[@aria-label='Choose Offer Start Date']")
    CURRENT_MONTH_DATES = (By.XPATH,"(//div[@class='grid grid-cols-7 gap-1'])[1]/button")
    DELETE_OFFER_BUTTON = (By.XPATH, "(//button)[27]")
    DELETE_OFFER_YES_BUTTON = (By.XPATH, "//button[normalize-space()='Yes']")
    DUPLICATE_OFFER_YES_BUTTON = (By.XPATH, "//button[normalize-space()='Yes']")
    OFFER_END_DATE = (By.XPATH, "//input[@aria-label='Choose Offer End Date']")
    OFFER_TABLE = (By.CSS_SELECTOR, ".text-sm.text-primary-500")
    EDIT_OFFER_BUTTON = (By.XPATH, "//tbody/tr[1]/td[9]/div[1]/div[2]/a[1]")
    FIRST_CELL = (By.XPATH, "//tr[1]//td[2]")
    OFFER_TITLE = (By.XPATH, "//h1[normalize-space()='Offer']")
    TABLE_HEADER = (By.TAG_NAME, "//th")
    TABLE_START_DATE = (By.XPATH, "//tbody/tr[1]/td[4]")
    TABLE_END_DATE = (By.XPATH, "//tbody/tr[1]/td[5]")
    SEARCH_INPUT = (By.CSS_SELECTOR, "#campaign-search")
    TABLE_DROPDOWN = (By.TAG_NAME, "select")
    CREATE_OFFER_BTN = (By.XPATH, "//button[normalize-space()='Create Offer']")
    UPDATE_OFFER_BTN = (By.XPATH, "//button[normalize-space()='Update Offer']")
    FIRST_OFFER_NAME = (By.XPATH, "//tr[1]/td[3]/a")
    PUBLISHER_REQUEST_COLUMN = (By.XPATH,"//tr//td[8]//a")
    PUBLISHER_REQ_VIEW_BUTTON = (By.XPATH ,"(//button)[31]")
    POPUP_OFFER_DELETED = (By.XPATH, "//div[@role='alert']/div[1]")
    POPUP_OFFER_UPDATED =(By.XPATH, "//div[contains(text(),'Offer updated successfully')]")
    DUPLICATE_OFFER_BUTTON = (By.XPATH, "//tbody/tr[1]/td[9]/div[1]/div[4]/button[1]")
    STATUS_BUTTON = (By.XPATH, "//tbody/tr[1]/td[7]/div[1]")
    POPUP_STATUS_BTN = (By.XPATH, "//div[@role='alert']/div[2]")
    OFFER_EXPORT_BTN = (By.XPATH, "//p[contains(@class,'text-sm text-white')]")
    TABLE = (By.XPATH, "//div[@class='overflow-x-auto max-w-full']")
    TABLE_NEXT_BUTTON = (By.XPATH, "(//button[@class='p-2 rounded disabled:opacity-50 inline-flex items-center justify-center h-6 w-8 hover:bg-brand-500 hover:text-white'])[2]")


    def is_offer_table_visible(self):
        return self.element_displayed(self.OFFER_TABLE)

    def is_table_data_present(self):
        self.wait_for_non_empty_text(self.FIRST_CELL)
        return self.driver.find_element(*self.FIRST_CELL).text

    def select_table_count(self,count):
        element = self.driver.find_element(*self.TABLE_DROPDOWN)
        s = Select(element)
        s.select_by_visible_text(count)

    def select_country(self):
        self.do_click(self.COUNTRY_DROPDOWN)
        countries = self.driver.find_elements(*self.ALL_COUNTRY_OPTION)
        for country in countries:
            if country.text == Constant.CREATE_OFFER_COUNTRY:
                country.click()
                break

    def select_offer_start_date(self):
        self.do_click(self.OFFER_START_DATE)
        dates = self.driver.find_elements(*self.CURRENT_MONTH_DATES)
        for date in dates:
            if int(date.text) == Constant.CREATE_OFFER_START_DATE:
                date.click()
                break

    def select_offer_end_date(self):
        self.do_click(self.OFFER_END_DATE)
        dates = self.driver.find_elements(*self.CURRENT_MONTH_DATES)
        for date in dates:
            if int(date.text) == Constant.CREATE_OFFER_END_DATE:
                date.click()
                break

    def select_offer_visibility(self):
        if Constant.OFFER_VISIBILITY.lower() == "public":
            self.do_click(self.OFFER_VISIBILITY_PUBLIC)
        elif Constant.OFFER_VISIBILITY.lower() == "private":
            self.do_click(self.OFFER_VISIBILITY_PRIVATE)
        else:
            raise ValueError("Invalid offer visibility option, please select a valid option")

    def select_conversion_type(self):
        if Constant.CONVERSION_TYPE.lower() == "static":
            self.do_click(self.CONVERSION_TYPE_STATIC)
        elif Constant.CONVERSION_TYPE.lower() == "dynamic":
            self.do_click(self.CONVERSION_TYPE_DYNAMIC)
        else:
            raise ValueError("Invalid conversion type option, please select a valid option")

    def select_conversion_method(self):
        self.do_click(self.CONVERSION_METHOD)
        conversion = self.driver.find_elements(*self.ALL_CONVERSION_DROPDOWN)
        for c in conversion:
            if c.text == Constant.CONVERSION_METHOD:
                c.click()
                break

    def select_call_timer_start(self):
        if Constant.CALL_TIMER_START.lower() == "incoming":
            self.do_click(self.CALL_TIMER_START_INCOMING)
        elif Constant.CALL_TIMER_START.lower() == "connected":
            self.do_click(self.CALL_TIMER_START_CONNECTED)
        elif Constant.CALL_TIMER_START.lower() == "dialed":
            self.do_click(self.CALL_TIMER_START_DIALLED)
        else:
            raise ValueError("Invalid call timer start option, please select a valid option")

    def select_payout_method(self):
        if Constant.PAYOUT_METHOD.lower() == "cpl":
            self.do_click(self.PAYOUT_METHOD_CPL)
        elif Constant.PAYOUT_METHOD.lower() == "cpa":
            self.do_click(self.PAYOUT_METHOD_CPA)
        elif Constant.PAYOUT_METHOD.lower() == "rev share":
            self.do_click(self.PAYOUT_METHOD_REV_SHARE)
        else:
            raise ValueError("Invalid payout method option, please select a valid option")

    def select_duplicate_timeframe(self):
        if Constant.DUPLICATE_TIMEFRAME.lower() == "enabled":
            self.do_click(self.DUPLICATE_TIMEFRAME_ENABLE)
        elif Constant.DUPLICATE_TIMEFRAME.lower() == "disabled":
            self.do_click(self.DUPLICATE_TIMEFRAME_disable)
        elif Constant.DUPLICATE_TIMEFRAME.lower() == "time limit":
            self.do_click(self.DUPLICATE_TIMEFRAME_TIMELIMIT)
        else:
            raise ValueError("Invalid duplicate timeframe option, please select a valid option")

    def get_offer_name_list(self):
        return self.get_elements_text_as_list(self.OFFER_NAME_COLUMN)

    def edit_country(self):
        self.do_click(self.COUNTRY_DROPDOWN)
        countries = self.driver.find_elements(*self.ALL_COUNTRY_OPTION)
        for country in countries:
            if country.text == Constant.EDIT_OFFER_COUNTRY:
                country.click()
                break

    def edit_offer_start_date(self):
        self.do_click(self.OFFER_START_DATE)
        dates = self.driver.find_elements(*self.CURRENT_MONTH_DATES)
        for date in dates:
            if int(date.text) == Constant.EDIT_OFFER_START_DATE:
                date.click()
                break

    def edit_offer_end_date(self):
        self.do_click(self.OFFER_END_DATE)
        dates = self.driver.find_elements(*self.CURRENT_MONTH_DATES)
        for date in dates:
            if int(date.text) == Constant.EDIT_OFFER_END_DATE:
                date.click()
                break

    def edit_offer_visibility(self):
        if Constant.EDIT_OFFER_VISIBILITY.lower() == "public":
            self.do_click(self.OFFER_VISIBILITY_PUBLIC)
        elif Constant.EDIT_OFFER_VISIBILITY.lower() == "private":
            self.do_click(self.OFFER_VISIBILITY_PRIVATE)
        else:
            raise ValueError("Invalid offer visibility option, please select a valid option")

    def edit_conversion_type(self):
        if Constant.EDIT_CONVERSION_TYPE.lower() == "static":
            self.do_click(self.CONVERSION_TYPE_STATIC)
        elif Constant.EDIT_CONVERSION_TYPE.lower() == "dynamic":
            self.do_click(self.CONVERSION_TYPE_DYNAMIC)
        else:
            raise ValueError("Invalid conversion type option, please select a valid option")

    def edit_conversion_method(self):
        self.do_click(self.CONVERSION_METHOD)
        conversion = self.driver.find_elements(*self.ALL_CONVERSION_DROPDOWN)
        for c in conversion:
            if c.text == Constant.EDIT_CONVERSION_METHOD:
                c.click()
                break

    def edit_call_timer_start(self):
        if Constant.EDIT_CALL_TIMER_START.lower() == "incoming":
            self.do_click(self.CALL_TIMER_START_INCOMING)
        elif Constant.EDIT_CALL_TIMER_START.lower() == "connected":
            self.do_click(self.CALL_TIMER_START_CONNECTED)
        elif Constant.EDIT_CALL_TIMER_START.lower() == "dialed":
            self.do_click(self.CALL_TIMER_START_DIALLED)
        else:
            raise ValueError("Invalid call timer start option, please select a valid option")

    def edit_payout_method(self):
        if Constant.EDIT_PAYOUT_METHOD.lower() == "cpl":
            self.do_click(self.PAYOUT_METHOD_CPL)
        elif Constant.EDIT_PAYOUT_METHOD.lower() == "cpa":
            self.do_click(self.PAYOUT_METHOD_CPA)
        elif Constant.EDIT_PAYOUT_METHOD.lower() == "rev share":
            self.do_click(self.PAYOUT_METHOD_REV_SHARE)
        else:
            raise ValueError("Invalid payout method option, please select a valid option")

    def edit_duplicate_timeframe(self):
        if Constant.EDIT_DUPLICATE_TIMEFRAME.lower() == "enabled":
            self.do_click(self.DUPLICATE_TIMEFRAME_ENABLE)
        elif Constant.EDIT_DUPLICATE_TIMEFRAME.lower() == "disabled":
            self.do_click(self.DUPLICATE_TIMEFRAME_disable)
        elif Constant.EDIT_DUPLICATE_TIMEFRAME.lower() == "time limit":
            self.do_click(self.DUPLICATE_TIMEFRAME_TIMELIMIT)
        else:
            raise ValueError("Invalid duplicate timeframe option, please select a valid option")

    def get_all_pages_as_dataframe(self):
        return self.extract_all_pages_as_dataframe(self.TABLE, self.TABLE_NEXT_BUTTON, exclude_last_n=2)