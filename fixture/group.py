
class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("new").click()
        self.fill_form_group(group)
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()
        wd.find_element_by_link_text("home").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.selected_first_group()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        wd.find_element_by_link_text("home").click()

    def selected_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.selected_first_group()
        wd.find_element_by_name("edit").click()
        self.fill_form_group(new_group_data)
        wd.find_element_by_name("update").click()
        self.return_to_group_page()

    def fill_form_group(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field).clear()
            wd.find_element_by_name(field).send_keys(text)

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))