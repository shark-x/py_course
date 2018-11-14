import re
from random import randrange
from model.contact import Contact


# def test_contact_info_on_home_page(app, db):
#     if len(db.get_contact_list()) == 0:
#         app.contact.create(Contact(firstname="FIRSTNAME", tmobile="123456789"))
#     contact_list_on_hp = app.contact.get_contact_list()
#     index = randrange(len(contact_list_on_hp))
#     contact_info_on_hp = contact_list_on_hp[index]
#     contact_info_on_ep = app.contact.get_contact_info_from_edit_page(index)
#     assert contact_info_on_hp.lastname == contact_info_on_ep.lastname
#     assert contact_info_on_hp.firstname == contact_info_on_ep.firstname
#     assert contact_info_on_hp.address == is_none(contact_info_on_ep.address)
#     assert contact_info_on_hp.all_emails_from_home_page == merge_emails_like_on_home_page(contact_info_on_ep)
#     assert contact_info_on_hp.all_phones_from_home_page == merge_phones_like_on_home_page(contact_info_on_ep)


#Сравнение информации о контактах/ Сравнивается информация со страницы изменения контакта с информацией загруженной из БД
def test_contact_info_on_edit_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="FIRSTNAME", tmobile="123456789"))
    contact_list_on_hp = db.get_contact_info()
    for contact_info_on_hp in contact_list_on_hp:
        # contact_info_on_ep = app.contact.get_contact_info_from_edit_page(index)
        contact_info_on_ep = app.contact.get_contact_info_from_edit_page_by_id(contact_info_on_hp.id)
        assert contact_info_on_hp.lastname == is_none(contact_info_on_ep.lastname)
        assert contact_info_on_hp.firstname == is_none(contact_info_on_ep.firstname)
        assert contact_info_on_hp.address == is_none(contact_info_on_ep.address)
        assert contact_info_on_hp.email == is_none(contact_info_on_ep.email)
        assert contact_info_on_hp.email2 == is_none(contact_info_on_ep.email2)
        assert contact_info_on_hp.email3 == is_none(contact_info_on_ep.email3)
        assert contact_info_on_hp.email3 == is_none(contact_info_on_ep.email3)
        assert contact_info_on_hp.thome == is_none(contact_info_on_ep.thome)
        assert contact_info_on_hp.tmobile == is_none(contact_info_on_ep.tmobile)
        assert contact_info_on_hp.twork == is_none(contact_info_on_ep.twork)
        assert contact_info_on_hp.sechome == is_none(contact_info_on_ep.sechome)
        # assert contact_info_on_hp.all_emails_from_home_page == merge_emails_like_on_home_page(contact_info_on_ep)
        # assert contact_info_on_hp.all_phones_from_home_page == merge_phones_like_on_home_page(contact_info_on_ep)


#Сравнение информации о контактах/ Сравнивается информация с главной страницы с информацией загруженной из БД
def test_contact_info_on_home_page(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="FIRSTNAME", tmobile="123456789"))
    contact_list_on_hp = app.contact.get_contact_list()
    contact_list_in_db = db.get_contact_info()
    for contact_info_on_hp in contact_list_on_hp:
        for contact_info_in_db in contact_list_in_db:
            if contact_info_on_hp.id == contact_info_in_db.id:
                assert contact_info_on_hp.lastname == contact_info_in_db.lastname
                assert contact_info_on_hp.firstname == contact_info_in_db.firstname
                assert contact_info_on_hp.address == is_none(contact_info_in_db.address)
                assert contact_info_on_hp.all_emails_from_home_page == merge_emails_like_on_home_page(contact_info_in_db)
                assert contact_info_on_hp.all_phones_from_home_page == merge_phones_like_on_home_page(contact_info_in_db)

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
