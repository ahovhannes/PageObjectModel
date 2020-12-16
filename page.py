from element import BasePageElement
from locators import EnrollPageLocators
from locators import MembersPageLocators

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class EnrollPage(BasePage):
    """Enroll page action methods come here"""

    css_class_pristine = "ng-pristine" #Field was pristine

    def is_name_field_filled(self):
        css_class_name = self.driver.find_element(*EnrollPageLocators.INPUT_NAME).get_attribute("class")
        if css_class_name.find(self.css_class_pristine) == -1:
            return False
        else:
            return True

    def is_birthday_field_filled(self):
        css_class_birthDate = self.driver.find_element(*EnrollPageLocators.INPUT_BIRTHDAY).get_attribute("class")
        if css_class_birthDate.find(self.css_class_pristine) == -1:
            return False
        else:
            return True

    def is_affinity_choosed(self):
        css_class_affinity = self.driver.find_element(*EnrollPageLocators.SELECT_AFFINITY).get_attribute("class")
        if css_class_affinity.find(self.css_class_pristine) == -1:
            return False
        else:
            return True

    def is_power_choosed(self):
        css_class_power = self.driver.find_element(*EnrollPageLocators.SELECT_AFFINITY).get_attribute("class")
        if css_class_power.find(self.css_class_pristine) == -1:
            return False
        else:
            return True

    def is_agrement_checkbox_checked(self):
        css_agrement_checkbox = self.driver.find_element(*EnrollPageLocators.CHECKBOX_AGREMENT).get_attribute("class")
        if css_agrement_checkbox.find(self.css_class_pristine) == -1:
            return False
        else:
            return True

    def is_title_matches(self):
        """Verifies that the hardcoded text "CaseStudy" appears in page title"""
        return "CaseStudy" in self.driver.title

    def is_power_dependet_from_affinity_correctly(self):
        dependency = True
        choose_affinity = self.driver.find_element(*EnrollPageLocators.SELECT_AFFINITY)
        for option_affinity in choose_affinity.find_elements_by_tag_name('option'):
            option_affinity.click()
            choose_power = self.driver.find_element(*EnrollPageLocators.SELECT_POWER)
            is_enabled_optgroup_power = choose_power.find_element_by_xpath("//optgroup[@label='"+option_affinity.text+"']").is_enabled()
            if not is_enabled_optgroup_power:
                print ".....ERROR: Not selectable option for '"+option_affinity.text+"' into 'power'"
                dependency = False
        if dependency:
            print "....True selections presented for binded selectors."
        return dependency

    def links_in_enroll_page(self):
        navbar_enroll = self.driver.find_element(*EnrollPageLocators.NAVBAR_ENROLL)
        enroll_page_links =  navbar_enroll.find_elements_by_tag_name("a")
        return enroll_page_links

    def type_name(self, name):
        input_name = self.driver.find_element(*EnrollPageLocators.INPUT_NAME)
        input_name.send_keys(name)

    def type_birthday(self, birthday):
        input_birthday = self.driver.find_element(*EnrollPageLocators.INPUT_BIRTHDAY)
        input_birthday.send_keys(birthday)

    def choose_affinity(self, choosed_affinity_option):
        """Choosing 'Earth' from 'Affinity'"""
        choose_affinity = self.driver.find_element(*EnrollPageLocators.SELECT_AFFINITY)
        for option in choose_affinity.find_elements_by_tag_name('option'):
            if option.text == choosed_affinity_option:
                option.click()
                break

    def choose_power_dependet_affinity(self, choosed_affinity_option):
        """Choosing appropriate values from the 'Power'"""
        choose_power = self.driver.find_element(*EnrollPageLocators.SELECT_POWER)
        #for option in choose_power.find_elements_by_tag_name('option'):
        #    if option.text == choosed_option:
        #        option.click() # select() in earlier versions of webdriver
        #        break
        for option in choose_power.find_element_by_xpath('//optgroup[@label="'+choosed_affinity_option+'"]').find_elements_by_tag_name('option'):
            option.click()

    def click_on_checkbox_agrement(self):
        checkbox_agrement = self.driver.find_element(*EnrollPageLocators.CHECKBOX_AGREMENT)
        checkbox_agrement.click()

    def click_submit_button(self):
        """Triggers the registration"""
        element = self.driver.find_element(*EnrollPageLocators.SUBMIT_BUTTON)
        element.click()


class MembersPage(BasePage):
    """Members page action methods come here"""

    def links_in_members_page(self):
        navbar_members = self.driver.find_element(*MembersPageLocators.NAVBAR_MEMBERS)
        members_page_links =  navbar_members.find_elements_by_tag_name("a")
        return members_page_links

    def is_users_table_presented(self):
        try:
            users_table = self.driver.find_element(*MembersPageLocators.USERS_TABLE)
        except NoSuchElementException:
            return False
        return True

    def has_users_table_true_columns(self):
        users_table_cols_expected = ["#", "Name", "Birth Date", "Affinity"]
        users_table_cols = self.driver.find_elements(*MembersPageLocators.USERS_TABLE_COLUMNS)
        L_users_table_cols = len(users_table_cols)
        for i in range(L_users_table_cols):
            users_table_cols_expected[i] = users_table_cols_expected[i].encode("utf-8")
            users_table_cols[i]          = users_table_cols[i].text.encode("utf-8")
            #print ">>>>>"+users_table_cols[i]+"    expected->>>>>"+users_table_cols_expected[i]
        if users_table_cols==users_table_cols_expected:
            return True
        else:
            return False

    def get_table_last_row(self):
        table_last_row = self.driver.find_element(*MembersPageLocators.USERS_TABLE_LAST_ROW).text
        table_last_row_arr = table_last_row.split()
        Number    = table_last_row_arr[0]
        Name      = table_last_row_arr[1]
        BirthDate = table_last_row_arr[2]
        Affinity  = table_last_row_arr[3]
        Power     = table_last_row_arr[4]
        return Number, Name, BirthDate, Affinity, Power















