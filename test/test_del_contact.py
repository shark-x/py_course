from model.contact import Contact


def test_del_first_contact(app):
    old_contact_list = app.contact.get_contact_list()
    contact = Contact(firstname="FIRSTNAME", tmobile="123456789")
    if app.contact.count() == 0:
        app.contact.create(contact)
    app.contact.delete()
    assert len(old_contact_list) - 1 == app.contact.count()
    # new_contact_list = app.contact.get_contact_list()
