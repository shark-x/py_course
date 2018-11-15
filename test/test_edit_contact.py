from model.contact import Contact
from random import randrange


def test_edit_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="abcd"))
    old_contact_list = db.get_contact_list()
    contact = Contact(firstname="a", middlename="b", lastname="c")
    index = randrange(len(old_contact_list))
    old_contact = old_contact_list[index]  # для отладки
    contact.id = old_contact_list[index].id
    # app.contact.edit_contact_by_index(contact, index)
    app.contact.edit_contact_by_id(contact, contact.id)
    assert len(old_contact_list) == len(db.get_contact_list())
    new_contact_list = db.get_contact_list()
    old_contact_list[index] = contact
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)



# def test_edit_first_contact_name(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="abcd"))
#     app.contact.edit(Contact(firstname="edif firstname", middlename="edit middle name", lastname="edit last name"))
#
#
# def test_edit_first_contact_address(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="abcd"))
#     app.contact.edit(Contact(address="edit only address"))
