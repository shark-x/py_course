import re
from random import randrange


def test_contact_info_on_home_page(app):
    contact_list_on_hp = app.contact.get_contact_list()
    index = randrange(len(contact_list_on_hp))
    contact_info_on_hp = contact_list_on_hp[index]
    contact_info_on_ep = app.contact.get_contact_info_from_edit_page(index)
    assert contact_info_on_hp.lastname == contact_info_on_ep.lastname
    assert contact_info_on_hp.firstname == contact_info_on_ep.firstname
    assert contact_info_on_hp.address == is_none(contact_info_on_ep.address)
    assert contact_info_on_hp.all_emails_from_home_page == merge_emails_like_on_home_page(contact_info_on_ep)
    assert contact_info_on_hp.all_phones_from_home_page == merge_phones_like_on_home_page(contact_info_on_ep)


def clear(s):
    return re.sub("[() -]", "", s)


def is_none(s):
    if s == None:
        return ""
    else:
        return s


def merge_phones_like_on_home_page(contact_info):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact_info.thome, contact_info.tmobile, contact_info.twork,
                                        contact_info.sechome]))))


def merge_emails_like_on_home_page(contact_info):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact_info.email, contact_info.email2, contact_info.email3]))))
