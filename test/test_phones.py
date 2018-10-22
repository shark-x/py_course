import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.thome == contact_from_edit_page.thome
    assert contact_from_view_page.twork == contact_from_edit_page.twork
    assert contact_from_view_page.tmobile == contact_from_edit_page.tmobile
    assert contact_from_view_page.sechome == contact_from_edit_page.sechome


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact_info):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact_info.thome,  contact_info.tmobile, contact_info.twork, contact_info.sechome]))))

