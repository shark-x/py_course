# -*- coding: utf-8 -*-
from model.contact import Contact


# @pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, db, json_contacts):
    contact = json_contacts
    old_contact_list = db.get_contact_list()
    app.contact.create(contact)
    assert len(old_contact_list) + 1 == app.contact.count()
    new_contact_list = db.get_contact_list()
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)


# @pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
# def test_add_contact(app, db, json_contacts):
#     contact = json_contacts
#     old_contact_list = app.contact.get_contact_list()
#     app.contact.create(contact)
#     assert len(old_contact_list) + 1 == app.contact.count()
#     new_contact_list = app.contact.get_contact_list()
#     old_contact_list.append(contact)
#     assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)