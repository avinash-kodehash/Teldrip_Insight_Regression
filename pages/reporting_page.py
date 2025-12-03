from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import BasePage

class Reporting(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.num = []

    DATE_RANGE = (By.XPATH, "//div[@class='relative h-full']//button//p[1]")
    DATE_THIS_MONTH = (By.XPATH, "//p[normalize-space()='This Month']")
    DATE_LAST_MONTH = (By.XPATH, "//p[normalize-space()='Last Month']")
    DATE_THIS_YEAR = (By.XPATH, "//p[normalize-space()='This Year']")
    DATE_LAST_YEAR = (By.XPATH, "//p[normalize-space()='Last Year']")
    DATE_LAST_7_DAYS = (By.XPATH, "//p[normalize-space()='Last 7 Days']")
    DATE_TODAY = (By.XPATH, "//p[normalize-space()='Today']")
    DATE_YESTERDAY = (By.XPATH, "//p[normalize-space()='Yesterday']")
    DATE_LAST_WEEK = (By.XPATH, "//p[normalize-space()='Last Week']")
    DATE_THIS_WEEK = (By.XPATH, "//p[normalize-space()='This Week']")
    CALL_DETAILS_TAB = (By.XPATH,"//button[normalize-space()='Call Details']")
    CALL_DETAILS_DATA = (By.CSS_SELECTOR,".overflow-x-auto.max-w-full")
    CAMPAIGN_TAB = (By.XPATH,"//button[normalize-space()='Campaign']")
    DATA = (By.CSS_SELECTOR,".text-sm.text-primary-500")
    PUBLISHER_TAB = (By.XPATH,"//button[normalize-space()='Publisher']")
    ADVERTISER_TAB = (By.XPATH,"//button[normalize-space()='Advertiser']")
    DESTINATION_TAB = (By.XPATH,"//button[normalize-space()='Destination']")
    CALLER_ID_TAB = (By.XPATH,"//button[normalize-space()='Caller ID']")
    DIALLED_NO_TAB = (By.XPATH,"//button[normalize-space()='Dialed No']")
    REFRESH_BUTTON = (By.CSS_SELECTOR,"button[class='bg-brand-500 border-0 justify-center rounded-md text-white text-xl inline-flex items-center md:rounded-xl md:size-14 size-12']")
    #Calls locators(call volume trend chart)
    INCOMING_CALLS = (By.CSS_SELECTOR,".apexcharts-legend-text[rel='1']")
    CONNECTED_CALLS = (By.CSS_SELECTOR,".apexcharts-legend-text[rel='2']")
    NOT_CONNECTED_CALLS = (By.CSS_SELECTOR,".apexcharts-legend-text[rel='3']")
    CONVERTED_CALLS = (By.CSS_SELECTOR,".apexcharts-legend-text[rel='4']")
    HANGUP_CALLS = (By.CSS_SELECTOR,".apexcharts-legend-text[rel='5']")
    BLOCKED_CALLS = (By.CSS_SELECTOR,".apexcharts-legend-text[rel='6']")
    CALL_TREND_CHART = (By.CSS_SELECTOR,"button[class='bg-brand-500 border-0 justify-center rounded-md text-white text-xl inline-flex items-center md:rounded-xl md:size-14 size-12']")
    #Call status overview chart
    CSO_INCOMING_CALLS = (By.XPATH, "(//p[contains(@class,'m-0 font-bold content-primary')])[1]")
    CSO_CONNECTED_CALLS = (By.XPATH,"(//p[contains(@class,'m-0 font-bold content-primary')])[2]")
    CSO_CONVERTED_CALLS = (By.XPATH,"(//p[contains(@class,'m-0 font-bold content-primary')])[3]")
    CSO_COMPLETED_CALLS = (By.XPATH,"(//p[contains(@class,'m-0 font-bold content-primary')])[4]")
    CSO_DUPLICATE_CALLS = (By.XPATH,"(//p[contains(@class,'m-0 font-bold content-primary')])[5]")
    #Call dropped chart
    CD_NOT_CONNECTED_CALLS = (By.XPATH,"(//p[contains(@class,'m-0 font-bold content-primary')])[6]")
    CD_HANGUP_CALLS = (By.XPATH,"(//p[contains(@class,'m-0 font-bold content-primary')])[7]")
    CD_BLOCKED_CALLS = (By.XPATH,"(//p[contains(@class,'m-0 font-bold content-primary')])[9]")
    CD_SYS_HANGUP_CALLS = (By.XPATH,"(//p[contains(@class,'m-0 font-bold content-primary')])[8]")

    TOTAL_CALLS = (By.XPATH,"(//div[contains(@class,'rounded-xl card-primary col-span-1 px-6 py-4 flex flex-col justify-center')])[1]/p[2]")
    #Finincials
    REVENUE = (By.CSS_SELECTOR,"div[class='flex items-start gap-3 sm:px-6 py-4 sm:py-8 xl:py-0 border-b sm:border-r xl:border-b-0 border-brand-secondary'] h3[class='text-2xl font-bold']")
    PAYOUT = (By.CSS_SELECTOR,"div[class='flex items-start gap-3 sm:px-6 py-4 sm:py-8 xl:py-0 border-b xl:border-r xl:border-b-0 border-brand-secondary'] h3[class='text-2xl font-bold']")
    GROSS_PROFIT = (By.CSS_SELECTOR,"div[class='flex items-start gap-3 sm:px-6 py-4 sm:py-8 xl:py-0 border-b sm:border-r sm:border-b-0 border-brand-secondary'] h3[class='text-2xl font-bold']")
    EXPENSE = (By.CSS_SELECTOR,"div[class='flex items-start gap-3 sm:px-6 py-4 sm:py-8 xl:py-0 undefined'] h3[class='text-2xl font-bold']")
    NET_PROFIT = (By.CSS_SELECTOR,"div[class='flex items-start gap-3 sm:px-6 py-4 sm:py-8 xl:py-0 lg:!px-0 '] h3[class='text-2xl font-bold']")
    EXPORT_BUTTON = (By.XPATH, "//button[normalize-space()='Export']")
    EXPORT_ALL_ROWS = (By.XPATH,"(//div[contains(@class,'size-6 min-w-6 rounded-full border-2 flex items-center justify-center transition-colors border-gray-400')])[1]")
    EXPORT_THIS_PAGE = (By.XPATH, "(//div[contains(@class,'size-6 min-w-6 rounded-full border-2 flex items-center justify-center transition-colors border-brand-500')])[1]")
    EXPORT_SUB_BUTTON = (By.XPATH, "(//div[@class='px-4 py-4 text-base rounded-lg content-primary ibf-bg-white-to-brand text-center '])[1]")
    EXPORT_SUB_BUTTON_ALL_DATA = (By.XPATH,"(//button[@class='px-4 py-4 text-base rounded-lg content-primary ibf-bg-white-to-brand text-center '])[1]")
    TABLE = (By.XPATH, "//div[@class='overflow-x-auto max-w-full']")
    TABLE_DROP_DOWN = (By.XPATH, "//select")
    FIRST_CELL = (By.XPATH, "//tr[1]//td[4]")
    TABLE_NEXT_BUTTON = (By.XPATH, "//div[@id='insights']//button[@class='p-2 rounded disabled:opacity-50 inline-flex items-center justify-center h-6 w-8 hover:bg-brand-500 hover:text-white'][2]")

    def is_table_data_present(self):
        self.logger.info("Checking if table data is present in reporting page")
        self.wait_for_non_empty_text(self.FIRST_CELL)
        data = self.driver.find_element(*self.FIRST_CELL).text
        self.logger.info(f"Table data found: {data}")
        return data

    def set_date(self, date_range):
        self.logger.info(f"Setting date range to: {date_range}")
        if date_range=="last month":
            self.do_click(self.DATE_RANGE)
            self.do_click(self.DATE_LAST_MONTH)
        elif date_range=="this month":
            self.do_click(self.DATE_RANGE)
            self.do_click(self.DATE_THIS_MONTH)
        elif date_range=="last year":
            self.do_click(self.DATE_RANGE)
            self.do_click(self.DATE_LAST_YEAR)
        elif date_range=="this year":
            self.do_click(self.DATE_RANGE)
            self.do_click(self.DATE_THIS_YEAR)
        elif date_range=="last 7 days":
            self.do_click(self.DATE_RANGE)
            self.do_click(self.DATE_LAST_7_DAYS)
        elif date_range=="today":
            self.do_click(self.DATE_RANGE)
            self.do_click(self.DATE_TODAY)
        elif date_range=="yesterday":
            self.do_click(self.DATE_RANGE)
            self.do_click(self.DATE_YESTERDAY)
        elif date_range=="last week":
            self.do_click(self.DATE_RANGE)
            self.do_click(self.DATE_LAST_WEEK)
        elif date_range=="this week":
            self.do_click(self.DATE_RANGE)
            self.do_click(self.DATE_THIS_WEEK)
        else:
            self.logger.error(f"Invalid date range option: {date_range}")
            raise ValueError("Invalid date range option, please select a valid option")
        self.logger.info(f"Date range set successfully to: {date_range}")

    def get_call_values_as_list(self, calls_locators):
        self.logger.info(f"Extracting call values from {len(calls_locators)} locators")
        for call in calls_locators:
            text = self.get_element_text(call)
            value = int(text.split("-")[-1].strip())
            self.num.append(value)
        self.logger.info(f"Extracted call values: {self.num}")

    def get_table_as_dataframe(self):
        self.logger.info("Extracting reporting table as dataframe")
        return self.extract_table_as_dataframe(self.TABLE, exclude_last_n=2)

    def get_all_pages_as_dataframe(self):
        self.logger.info("Extracting all pages of reporting table as dataframe")
        return self.extract_all_pages_as_dataframe(self.TABLE, self.TABLE_NEXT_BUTTON, exclude_last_n=2)

    def select_table_dropdown(self, value):
        self.logger.info(f"Selecting table dropdown value: {value}")
        #self.scroll_to_element(self.TABLE_DROP_DOWN)
        dropdown = self.driver.find_element(*self.TABLE_DROP_DOWN)
        select = Select(dropdown)
        select.select_by_value(value)
        self.logger.info(f"Table dropdown value {value} selected successfully")
