# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from selenium.webdriver.support.select import Select
from group import Group
from contact import Contact

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_group_page(wd)
        self.create_group(wd, Group(name="name group", header="11111", footer="22222"))
        # Return to groups page
        wd.find_element_by_link_text("group page").click()
        # Logout
        wd.find_element_by_link_text("Logout").click()

    def test_add_empty_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_group_page(wd)
        self.create_group(wd, Group(name="", header="", footer=""))
        # Return to groups page
        wd.find_element_by_link_text("group page").click()
        # Logout
        wd.find_element_by_link_text("Logout").click()

    def create_group(self, wd, group):
        # Init group creation
        wd.find_element_by_name("new").click()
        # Fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Submit group creation
        wd.find_element_by_name("submit").click()

    def open_group_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

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


class TestAddContacts(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contacts(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username='admin', password='secret')
        self.contact_creation(wd, firstname="aaaaaa", middlename="aaaaaaa", lastname="aaaaaaaaa", nickname="bbbbbbbbbbbb",
                              title="wert", company="qwert", address="qwertyuiop[]asdfghjkl;zxcvbnm,./",
                              thome="dfghjkl;", tmobile="1234567890", twork="dfghjkl", tfax="567gfh",
                              email="123@jdjj.com", secaddress="sssssssssss", sechome="eeeeeeeeee", secnote="eeeeeeeeeeeeee",
                              email2="1ggg@gh.com", email3="hhhh@hh.hh", bday="17", bmonth="November", byear="1998",
                              aday="12", amonth="November", ayear="2222")
        # Submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        # Logout
        wd.find_element_by_link_text("Logout").click()

    def contact_creation(self, wd, firstname, middlename, lastname, nickname, title, company, address, thome, tmobile,
                         twork, tfax, email, secaddress, sechome, secnote, email2, email3, bday, bmonth, byear, aday,
                         amonth, ayear):
        # Init contact creation
        wd.find_element_by_link_text("add new").click()
        # Fill contact form
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(nickname)
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(company)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(thome)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(tmobile)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(twork)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(tfax)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(email)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(bday)
        wd.find_element_by_xpath("//option[@value='17']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(bmonth)
        wd.find_element_by_xpath("//option[@value='November']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(byear)
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(secaddress)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(sechome)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(secnote)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(aday)
        wd.find_element_by_xpath("(//option[@value='12'])[2]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(amonth)
        wd.find_element_by_xpath("(//option[@value='November'])[2]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(ayear)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(email2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(email3)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("jk.com")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

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
