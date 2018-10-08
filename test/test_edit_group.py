from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.edit_first_group(Group(name="editname", header="editheader", footer="editfooter"))
    # app.group.delete_first_group()


def test_edit_first_group_only_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.edit_first_group(Group(name="editname"))
