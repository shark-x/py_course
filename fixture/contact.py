
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_form_contact(contact)
        # Submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_home_page()

    def return_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/") and len(wd.find_elements_by_css_selector("img[alt=\"Edit\"]")) > 0):
            wd.find_element_by_link_text("home").click()

    def details_contact(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("img[alt=\"Details\"]").click()
        self.return_home_page()

    def edit(self, new_contact_data):
        wd = self.app.wd
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        self.fill_form_contact(new_contact_data)
        # Submit contact creation
        wd.find_element_by_name("update").click()
        self.return_home_page()

    def delete(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_home_page()

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





