from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="edit1", header="edit2", footer="edit3"))
    app.session.logout()


def test_edit_first_group_only_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="edithhhhhhhhhhhhhhhhhhhhh2"))
    app.session.logout()
