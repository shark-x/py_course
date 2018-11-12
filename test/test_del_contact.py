from model.contact import Contact
from random import randrange
import random


def test_del_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="FIRSTNAME", tmobile="123456789"))
    old_contact_list = db.get_contact_list()
    contact = random.choice(old_contact_list)
    app.contact.delete_contact_by_id(contact.id)
    new_contact_list = db.get_contact_list()
    old_contact_list.remove(contact)
    assert old_contact_list == new_contact_list
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

# def test_del_some_contact(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="FIRSTNAME", tmobile="123456789"))
#     old_contact_list = app.contact.get_contact_list()
#     index = randrange(len(old_contact_list))
#     app.contact.delete_contact_by_index(index)
#     assert len(old_contact_list) - 1 == app.contact.count()
#     new_contact_list = app.contact.get_contact_list()
#     old_contact_list[index:index+1] = []
#     assert old_contact_list == new_contact_list