from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    assert len(old_groups)-1 == app.group.count()
    # new_groups = app.group.get_group_list()

