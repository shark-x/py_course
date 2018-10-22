# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

# data_driven
test_data = [
        Contact(firstname="", middlename="", lastname="")]+[
        Contact(firstname=random_string("name", 10), middlename=random_string("header", 20), lastname=random_string("footer", 15))
        for i in range(5)
]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, contact):
    old_contact_list = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contact_list) + 1 == app.contact.count()
    new_contact_list = app.contact.get_contact_list()
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)

# def test_add_contact_empty(app):
#     app.contact.create(Contact(firstname="", middlename="", lastname="", nickname=""))
