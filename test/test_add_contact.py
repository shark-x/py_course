# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="anasa", middlename="middlename", lastname="lastname"))


def test_add_contact_empty(app):
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname=""))
