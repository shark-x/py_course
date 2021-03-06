from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("new").click()
        self.fill_form_group(group)
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()
        wd.find_element_by_link_text("home").click()
        self.group_cache = None

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        self.selected_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        wd.find_element_by_link_text("home").click()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_group_page()
        self.selected_group_by_id(id)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        wd.find_element_by_link_text("home").click()
        self.group_cache = None

    # def delete_first_group(self):
    #     self.delete_group_by_index(0)

    def selected_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def selected_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='%s']" % id).click()

    def edit_group_by_index(self, new_group_data, index):
        wd = self.app.wd
        self.open_group_page()
        self.selected_group_by_index(index)
        wd.find_element_by_name("edit").click()
        self.fill_form_group(new_group_data)
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None

    def edit_group_by_id(self, new_group_data, id_group):
        wd = self.app.wd
        self.open_group_page()
        index = self.get_group_index(id_group)
        self.selected_group_by_index(index)
        wd.find_element_by_name("edit").click()
        self.fill_form_group(new_group_data)
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None

    def get_group_index(self,id_group):
        wd = self.app.wd
        group_list = wd.find_elements_by_xpath("//span[@class='group']")
        for group in group_list:
            id = group.find_element_by_name("selected[]").get_attribute("value")
            if id == id_group:
                return group_list.index(group)

    def edit_first_group(self, new_group_data):
        self.edit_group_by_index(new_group_data, 0)

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

    # Возвращает длину списка групп
    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_xpath("//span[@class='group']"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)
