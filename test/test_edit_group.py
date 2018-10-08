from model.group import Group


def test_edit_first_group(app):
    app.group.edit_first_group(Group(name="edit1", header="edit2", footer="edit3"))


def test_edit_first_group_only_name(app):
    app.group.edit_first_group(Group(name="edithhhhhhhhhhhhhhhhhhhhh2"))
