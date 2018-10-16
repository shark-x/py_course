# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contact_list = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="anasa", middlename="middlename", lastname="lastname"))
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) + 1 == len(new_contact_list)


# def test_add_contact_empty(app):
#     app.contact.create(Contact(firstname="", middlename="", lastname="", nickname=""))
