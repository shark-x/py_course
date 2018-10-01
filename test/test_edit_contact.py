from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin",password="secret")
    app.contact.edit(Contact(firstname="Nas", middlename="Nasmiddlename", lastname="Naslastname", nickname="Nasnickname",
                            photo="C:\\Users\\Public\\Pictures\\shark.png", title="Nastitle", company="Nascompany",
                            address="Nasaddress",thome="Nastelhome", tmobile="Nastelmobile", twork="Nastelwork", fax="fax",
                            email="Nasemail", email2="Nasemail2", email3="Nasemail3", homepage="Nashomepage",
                            bday="20", bmonth="November", byear="1991",aday="18", amonth="September", ayear="2016",
                            secaddress="Nassecaddress", sechome="Nassechome", secnote="Nassecnote"))
    app.session.logout()
