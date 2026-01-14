from datetime import datetime


class Constant:

    #LOGIN
    USERNAME = "hariom.d@kodehash.com"
    PASSWORD = "KODEhash@000"
    # USERNAME = "demoaccount@yopmail.com"
    # PASSWORD = "KODEhash@000"
    # USERNAME = "meghna.c@kodehash.com"
    # PASSWORD = "KODEhash@000"
    BASE_URL = "https://devapp.teldrip.com/login"

    DATE_RANGE = "last month"
    BASE_API_URL = "https://admin.teldrip.com/"

    #OFFERINGS
    OFFER_SEARCH = "off"

    #CREATE OFFER
    CREATE_OFFER_COUNTRY = "India"
    CREATE_OFFER_NAME = "Ajay Offer_1"
    CREATE_OFFER_DESCRIPTION = ""
    CREATE_OFFER_START_DATE = datetime.now().day  # Today's day as integer (e.g., 27)
    CREATE_OFFER_END_DATE = datetime.now().day  # Today's day as integer (e.g., 27)
    OFFER_VISIBILITY = "Public"  # Options: "Public" or "Private"
    CONVERSION_TYPE = "static"  # Options: "Static" or "Dynamic"
    CONVERSION_METHOD = "Normal Conversion" # Options: "Normal Conversion" or "Direct Post Conversion or Ping Post Conversion"
    CALL_TIMER_START = "incoming" # Options: "incoming" or "connected" or "dialed"
    DURATION_IN_SECONDS = 10
    PAYOUT_METHOD = "cpl"  # Options: "cpl" or "cpa" or "rev share"
    PAYOUT_AMOUNT = 10
    DUPLICATE_TIMEFRAME = "enabled"  # Options: "enabled" or "disabled" or "time limit"(Time limit option not implemented)

    #Edit Offer
    EDIT_OFFER_NAME = "Edited Avinash Offer"
    EDIT_OFFER_DESCRIPTION = "This is edited description"
    EDIT_OFFER_COUNTRY = "India"
    EDIT_OFFER_START_DATE = datetime.now().day  # Today's day as integer (e.g., 27)
    EDIT_OFFER_END_DATE = datetime.now().day  # Today's day as integer (e.g., 27)
    EDIT_OFFER_VISIBILITY = "Private"  # Options: "Public" or "Private"
    EDIT_CONVERSION_TYPE = "dynamic"  # Options: "Static" or "Dynamic"
    EDIT_CONVERSION_METHOD = "Direct Post Conversion"  # Options: "Normal Conversion" or "Direct Post Conversion or Ping Post Conversion"
    EDIT_CALL_TIMER_START = "connected"  # Options: "incoming" or "connected" or "dialed"
    EDIT_DURATION_IN_SECONDS = 20
    EDIT_PAYOUT_METHOD = "cpa"  # Options: "cpl" or "cpa" or "rev share"
    EDIT_PAYOUT_AMOUNT = 20
    EDIT_DUPLICATE_TIMEFRAME = "disabled"  # Options: "enabled" or "disabled" or "time limit"(Time limit option not implemented)

    #Duplicate Offer
    DUP_OFFER_NAME = "Duplicate Avinash Offer"

    #User
    USER_EMAIL = "ajaypub2@yopmail.com"
    USER_ROLE = "Publisher"
    USER_COUNTRY = "India"
    USER_FIRST_NAME = "Ajay"
    USER_LAST_NAME = "Publisher"
    USER_COMPANY = "Automation"
    USER_COMPANY_ADDRESS = "Automation"
    USER_MOBILE = "2025550123"
    USER_COMPANY_WEBSITE = "https://www.automation.com"
    
