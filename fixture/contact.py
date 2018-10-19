from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_form_contact(contact)
        # Submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.open_home_page()
        self.contact_cache = None

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/") and len(wd.find_elements_by_css_selector('img[alt="Edit"]')) > 0):
            wd.find_element_by_link_text("home").click()

    def edit_contact_by_index(self, new_contact_data, index):
        wd = self.app.wd
        self.open_home_page()
        element = self.selected_contact_by_index(index)
        element.find_element_by_xpath("td[8]").click()
        self.fill_form_contact(new_contact_data)
        # Submit contact creation
        wd.find_element_by_name("update").click()
        self.open_home_page()
        self.contact_cache = None

    def selected_contact_by_index(self, index):
        wd = self.app.wd
        return wd.find_elements_by_xpath("//tr[@name='entry']")[index]

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        element = self.selected_contact_by_index(index)
        element.find_element_by_xpath("td[1]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def fill_form_contact(self, contact):
        # Name
        self.change_field_contact("firstname", contact.firstname)
        self.change_field_contact("middlename", contact.middlename)
        self.change_field_contact("lastname", contact.lastname)
        self.change_field_contact("nickname", contact.nickname)
        # Different information
        self.change_field_contact("photo", contact.photo)
        self.change_field_contact("title", contact.title)
        self.change_field_contact("company", contact.company)
        self.change_field_contact("address", contact.address)
        # Telephones and emails
        self.change_field_contact("home", contact.thome)
        self.change_field_contact("mobile", contact.tmobile)
        self.change_field_contact("work", contact.twork)
        self.change_field_contact("fax", contact.tfax)
        self.change_field_contact("email", contact.email)
        self.change_field_contact("email2", contact.email2)
        self.change_field_contact("email3", contact.email3)
        self.change_field_contact("homepage", contact.homepage)
        # Birthday and anniversary
        self.change_field_contact("bday", contact.bday)
        self.change_field_contact("bmonth", contact.bmonth)
        self.change_field_contact("byear", contact.byear)
        self.change_field_contact("aday", contact.aday)
        self.change_field_contact("amonth", contact.amonth)
        self.change_field_contact("ayear", contact.ayear)
        # wd.find_element_by_name("new_group").click()
        # wd.find_element_by_xpath("//option[@value='[none]']").click()
        # Secondary
        self.change_field_contact("address2", contact.secaddress)
        self.change_field_contact("phone2", contact.sechome)
        self.change_field_contact("notes", contact.secnote)

    def change_field_contact(self, field, text):
        wd = self.app.wd
        if text is not None:
            if field == "bday" or field == "bmonth" or field == "aday" or field == "amonth":
                wd.find_element_by_name(field).click()
                wd.find_element_by_name(field).send_keys(text)
            elif field == "photo":
                wd.find_element_by_name(field).send_keys(text)
            else:
                wd.find_element_by_name(field).click()
                wd.find_element_by_name(field).clear()
                wd.find_element_by_name(field).send_keys(text)

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                lastname = element.find_element_by_xpath("td[2]").text
                firstname = element.find_element_by_xpath("td[3]").text
                address = element.find_element_by_xpath("td[4]").text
                id = element.find_element_by_name("selected[]").get_attribute("id")
                all_emails = element.find_element_by_xpath("td[5]").text
                all_phones = element.find_element_by_xpath("td[6]").text
                self.contact_cache.append(Contact
                                          (lastname=lastname, firstname=firstname, address=address, id=id,
                                           all_emails_from_home_page=all_emails, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        id = wd.find_element_by_name("home").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        thome = wd.find_element_by_name("home").get_attribute("value")
        twork = wd.find_element_by_name("work").get_attribute("value")
        tmobile = wd.find_element_by_name("mobile").get_attribute("value")
        sechome = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(lastname=lastname, firstname=firstname, id=id,
                       email=email, email2=email2, email3=email3,
                       thome=thome, twork=twork, tmobile=tmobile, sechome=sechome)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        thome = re.search("H: (.*)", text).group(1)
        twork = re.search("W: (.*)", text).group(1)
        tmobile = re.search("M: (.*)", text).group(1)
        sechome = re.search("F: (.*)", text).group(1)
        return Contact(thome=thome, twork=twork, tmobile=tmobile, sechome=sechome)


