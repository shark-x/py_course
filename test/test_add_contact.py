# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits #+ " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_numder_string(prefix, maxlen):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_email_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    domen_list = ["ru", "com", "org"]
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@" +\
           "".join([random.choice(string.ascii_letters) for i in range(random.randrange(5))]) + "." + \
           random.choice(domen_list)


# data_driven
test_data = [
        Contact(firstname="", middlename="", lastname="")] + [
        Contact(firstname=random_string("firstname", 10), middlename=random_string("midname", 20), lastname=random_string("lastname", 15),
                address=random_string("address", 5),
                tmobile=random_numder_string("tmobile", 11), twork=random_numder_string("twork", 11),
                thome=random_numder_string("thome", 11), sechome=random_numder_string("sechome", 11),
                email=random_email_string("em1", 20), email2=random_email_string("em2", 20),
                email3=random_email_string("em3", 20))
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

