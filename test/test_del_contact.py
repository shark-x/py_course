from model.contact import Contact


def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="FIRSTNAME", tmobile="123456789"))
    app.contact.delete()
