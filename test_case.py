#
# This script created by Hovhannes Atoyan (hovhannes.atoyan@gmail.com)
# DEPENDENCY: Python 2.7; Selenium 2.53 compatible with FF45
#
#Specifications:
#  1. The website should consist of 2 pages: Enroll page and Members page.
#  2. On opening the main link, the user should be immediately redirected to the Enrollpage.
#  3. There should be a header with links to Enroll and Members pages in all the pages
#  4. Enroll page: The applicant should fill in the form with basic information (name,surname, birthdate, attribute, power) and agree to the terms and conditions.
#  5. Enroll page: All form fields are required/mandatory in order to submit the form.
#  6. Enroll page: The value of power field depends on the affinity field. For example: Avillain with affinity "Fire" can only choose powers "Meteor" and "Fire Spear" (orchoose both, because the field "Power" allows multiple selection).
#  7. Enroll page: After submitting the form, the user should be sent to the Members page.
#  8. Members page: User should see the data of the form he/she submitted, in themembers table.
#  9. Members page: There should be a table of all the villains enrolled.
#  10. Members page: The table should have 4 columns - Number, Name, Birth date, andAffinity
# 
import datetime
import unittest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import page
import time

class myTestCase(unittest.TestCase):
    def setUp(self):
        self.site_url = "http://qa-case-study.hydrane.com/"
        self.site_pages_arr = ["/register", "/members"]
        #self.driver = webdriver.Firefox()
        firefox_binary = FirefoxBinary("D:\Programs\Portables\__Browsers\FirefoxPortable_45.0.2\FirefoxPortable.exe")
        self.driver = webdriver.Firefox(firefox_binary=firefox_binary)
        self.driver.get(self.site_url)

    def tearDown(self):
        self.driver.close()

    def test_cases(self):
        print "\n..... Beginning test sequences ...\n"
        self.tc2()  # On opening the main link, the user should be immediately redirected to the Enrollpage
        self.tc1()  # Enroll and Members page existance into site
        self.tc3()  # Header with links to Enroll and Members pages in all the pages
        self.tc5()  # All form fields are required/mandatory
        self.tc6()  # The value of power field depends on the affinity field.
        self.tc4()  # Fill the form's fields and press submit
        self.tc7()  # Go to Members page after submitting the form
        self.tc9()  # Members page's table existance
        self.tc10() # The table should have 4 columns
        self.tc8()  # Data from submitted form presented into member's table

    def tc1(self):
        print "TC1. The website should consist of 2 pages: Enroll page and Members page."
        enroll_page = page.EnrollPage(self.driver)
        members_page = page.MembersPage(self.driver)
        for link_enroll in enroll_page.links_in_enroll_page():
            if not (link_enroll.get_attribute("routerlink") in self.site_pages_arr):
                print ".....ERROR: Wrong header link on the 'Enroll' page"
        for link_members in members_page.links_in_members_page():
            if not (link_members.get_attribute("routerlink") in self.site_pages_arr):
                print ".....ERROR: Wrong header link on the 'Members' page"
        print "----- TC1 done -----\n"

    def tc2(self):
        print "TC2. On opening the main link, the user should be immediately redirected to the Enrollpage."
        if self.driver.current_url==self.site_url+self.site_pages_arr[0][1:]:
            print "After the page loading... "
            print ".....Correct page '"+self.driver.current_url+"' presented for 'Enroll'"
        else:
            print ".....ERROR: Wrong page after the redirection."
        print "----- TC2 done -----\n"

    def tc3(self):
        print "TC3. There should be a header with links to Enroll and Members pages in all the pages."
        enroll_links_arr  = []
        members_links_arr = []
        enroll_page = page.EnrollPage(self.driver)
        for link_enroll in enroll_page.links_in_enroll_page():
            enroll_links_arr.append(link_enroll)
        members_page = page.MembersPage(self.driver)
        for link_members in members_page.links_in_members_page():
            members_links_arr.append(link_members)
        if enroll_links_arr==members_links_arr:
            print ".....Correct links for Enroll and Members pages"
        else:
            print ".....ERROR: Diferent links for Enroll and Members pages"
        print "----- TC3 done -----\n"

    def tc4(self):
        print "TC4. Enroll page: The applicant should fill in the form with basic information (name, birthdate, attribute, power) and agree to the terms and conditions."
        enroll_page = page.EnrollPage(self.driver)
        enroll_page.type_name("Test_Name_"+str(datetime.datetime.now()))
        enroll_page.type_birthday("1982-02-23")
        enroll_page.choose_affinity("Earth")
        enroll_page.choose_power_dependet_affinity("Earth")
        enroll_page.click_on_checkbox_agrement()
        #enroll_page.click_submit_button()
        print "----- TC4 done -----\n"

    def tc5(self):
        print "TC5. Enroll page: All form fields are required/mandatory in order to submit the form."
        enroll_page = page.EnrollPage(self.driver)
        assert enroll_page.is_name_field_filled(),     ".....ERROR: Not filled field 'Name'"
        assert enroll_page.is_birthday_field_filled(), ".....ERROR: Not filled field 'Birth Date'"
        assert enroll_page.is_affinity_choosed(), ".....ERROR: Not choosed select field 'Affinity'"
        assert enroll_page.is_power_choosed(),    ".....ERROR: Not choosed select field 'Power'"
        assert enroll_page.is_agrement_checkbox_checked(), ".....ERROR: Agrement checkbox not checked"
        print "----- TC5 done -----\n"

    def tc6(self):
        print "TC6. Enroll page: The value of power field depends on the affinity field. For example: Avillain with affinity 'Fire' can only choose powers 'Meteor' and 'Fire Spear'."
        enroll_page = page.EnrollPage(self.driver)
        enroll_page.is_power_dependet_from_affinity_correctly()
        print "----- TC6 done -----\n"

    def tc7(self):
        print "TC7. Enroll page: After submitting the form, the user should be sent to the Members page."
        enroll_page = page.EnrollPage(self.driver)
        enroll_page.click_submit_button()
        time.sleep(2)
        print "After submiting, we were redirected to page "+self.driver.current_url
        if self.driver.current_url==(self.site_url+self.site_pages_arr[1][1:]):
            print ".....This is correct location"
        else:
            print ".....ERROR: Wrong location after the submit button pressing" 
        print "----- TC7 done -----\n"

    def tc8(self):
        print "TC8. Members page: User should see the data of the form he/she submitted, in the members table."
        is_value_in_field = True
        members_page = page.MembersPage(self.driver)
        last_row_vals = members_page.get_table_last_row()
        Number    = last_row_vals[0]
        Name      = last_row_vals[1]
        BirthDate = last_row_vals[2]
        Affinity  = last_row_vals[3]
        Power     = last_row_vals[4]
        assert Number, ".....ERROR: No 'Number' into page "+self.site_url+self.site_pages_arr[1][1:]
        assert Name,   ".....ERROR: No 'Name' into page "+self.site_url+self.site_pages_arr[1][1:]
        assert BirthDate, ".....ERROR: No 'BirthDate' into page "+self.site_url+self.site_pages_arr[1][1:]
        assert Affinity,  ".....ERROR: No 'Affinity' into page "+self.site_url+self.site_pages_arr[1][1:]
        assert Power,     ".....ERROR: No 'Power' into page "+self.site_url+self.site_pages_arr[1][1:]
        print "----- TC8 done -----\n"

    def tc9(self):
        print "TC9. Members page: There should be a table of all the villains enrolled."
        members_page = page.MembersPage(self.driver)
        assert members_page.is_users_table_presented(), ".....ERROR: No users table in the page 'members'" 
        print "----- TC9 done -----\n"

    def tc10(self):
        print "TC10. Members page: The table should have 4 columns - Number, Name, Birth date, andAffinity"
        members_page = page.MembersPage(self.driver)
        assert members_page.has_users_table_true_columns(), ".....ERROR: Wrong columns for users table"
        print "----- TC10 done -----\n"


if __name__ == "__main__":
    unittest.main()

	
