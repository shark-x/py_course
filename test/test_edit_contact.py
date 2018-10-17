from model.contact import Contact


def test_edit_first_contact_all(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="abcd"))
    old_contact_list = app.contact.get_contact_list()
    contact = Contact(firstname="Nas", middlename="Nasmiddlename", lastname="Naslastname", nickname="Nasnickname")
    contact.id = old_contact_list[0].id
    app.contact.edit(contact)
    assert len(old_contact_list) == app.contact.count()
    new_contact_list = app.contact.get_contact_list()
    old_contact_list[0] = contact
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)

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
