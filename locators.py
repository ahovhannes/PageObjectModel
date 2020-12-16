from selenium.webdriver.common.by import By

class EnrollPageLocators(object):
    """A class for Enroll page locators. All Enroll page locators should come here"""
    NAVBAR_ENROLL     = (By.ID, "navbarSupportedContent")
    INPUT_NAME        = (By.NAME, 'name')
    INPUT_BIRTHDAY    = (By.NAME, 'birthDate')
    SELECT_AFFINITY   = (By.ID, 'affinity')
    SELECT_POWER      = (By.ID, 'power')
    CHECKBOX_AGREMENT = (By.NAME, 'selfish')
    SUBMIT_BUTTON     = (By.XPATH, "//button[@type='submit']")

class MembersPageLocators(object):
    """A class for Members page locators. All Members page locators should come here"""
    NAVBAR_MEMBERS       = (By.ID, "navbarSupportedContent")
    USERS_TABLE          = (By.XPATH, "//table[@class='table']")
    USERS_TABLE_COLUMNS  = (By.XPATH, "//table[@class='table']/thead/tr/th")
    USERS_TABLE_LAST_ROW = (By.CSS_SELECTOR, '.table > tbody > tr:last-child')


