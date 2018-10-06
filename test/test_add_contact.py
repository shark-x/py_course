# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(firstname="anasa", middlename="middlename", lastname="lastname", nickname="nickname",
                            photo="C:\\Users\\Public\\Pictures\\ананас.jpg", title="title", company="company", address="address",
                            thome="telhome", tmobile="telmobile", twork="telwork", fax="fax",
                            email="email", email2="email2", email3="email3",
                            homepage="homepage",
                            bday="15", bmonth="November", byear="1990",aday="18", amonth="September", ayear="2016",
                            secaddress="secaddress", sechome="sechome", secnote="secnote"))
    app.session.logout()
