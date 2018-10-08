from model.contact import Contact


def test_edit_first_contact_all(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="abcd"))
    app.contact.edit(Contact(firstname="Nas", middlename="Nasmiddlename", lastname="Naslastname", nickname="Nasnickname",
                            photo= "C:\\Users\\Public\\Pictures\\shark.png", title="Nastitle", company="Nascompany",
                            address="Nasaddress", thome="Nastelhome", tmobile="Nastelmobile", twork="Nastelwork", fax="fax",
                            email="Nasemail", email2="Nasemail2", email3="Nasemail3", homepage="Nashomepage",
                            bday="20", bmonth="November", byear="1991",aday="18", amonth="September", ayear="2016",
                            secaddress="Nassecaddress", sechome="Nassechome", secnote="Nassecnote"))
    # app.contact.delete()


def test_edit_first_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="abcd"))
    app.contact.edit(Contact(firstname="edif firstname", middlename="edit middle name", lastname="edit last name"))


def test_edit_first_contact_address(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="abcd"))
    app.contact.edit(Contact(address="edit only address"))
