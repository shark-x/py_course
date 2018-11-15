from model.group import Group
from random import randrange


def test_edit_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="editname", header="editheader", footer="editfooter")
    group.id = old_groups[index].id
    # app.group.edit_group_by_index(group, index)
    app.group.edit_group_by_id(group, group.id)
    assert len(old_groups) == len(db.get_group_list())
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

# def test_edit_first_group_only_name(app):
#     old_groups = app.group.get_group_list()
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     app.group.edit_first_group(Group(name="editname"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups
