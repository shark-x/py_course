# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contact import Contact


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_untitled_test_case(self):
        wd = self.wd
        # Open home page
        wd.get("http://localhost/addressbook/")
        self.login(wd, username="admin", password="secret")
        self.create_contact(wd, Contact(firstname="anasa", middlename="middlename", lastname="lastname", nickname="nickname",
                            photo="C:\\Users\\Public\\Pictures\\shark.png", title="title", company="company", address="address",
                            thome="telhome", tmobile="telmobile", twork="telwork", fax="fax",
                            email="email", email2="email2", email3="email3",
                            homepage="homepage",
                            bday="15", bmonth="November", byear="1990",aday="18", amonth="September", ayear="2016",
                            secaddress="secaddress", sechome="sechome", secnote="secnote"))
        # Logout
        wd.find_element_by_link_text("Logout").click()

    def create_contact(self, wd, contact):
        wd.find_element_by_link_text("add new").click()
        # Name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # Different information
        wd.find_element_by_name("photo").send_keys(contact.photo)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        # Telephones and emails
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.thome)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.tmobile)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.twork)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.tfax)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        # Birthday and anniversary
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bday").send_keys(contact.bday)
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("bmonth").send_keys(contact.bmonth)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        wd.find_element_by_name("aday").click()
        wd.find_element_by_name("aday").send_keys(contact.aday)
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_name("amonth").send_keys(contact.amonth)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ayear)
        wd.find_element_by_name("new_group").click()
        wd.find_element_by_xpath("//option[@value='[none]']").click()
        # Secondary
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.secaddress)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.sechome)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.secnote)
        # Submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def login(self, driver, username, password):
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()