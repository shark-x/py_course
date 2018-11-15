from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture
from model.group import Group


def test_add_some_contact_in_group(app, db, check_ui):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    try:
        if len(db.get_contact_list()) == 0:
            app.contact.create(Contact(firstname="abcd"))
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name='group', header='header_group', footer='footer_group'))
        # берем список групп из БД
        groups_list = db.get_group_list()
        # выбираем некоторую группу из списка
        group = random.choice(groups_list)
        # получаем из БД список контактов входящих в данную группу
        old_contacts_in_group = db.get_contacts_in_group(Group(id=group.id))
        # получаем из БД список контактов не входящих в данную группу
        contacts_not_in_group = db.get_contacts_not_in_group(Group(id=group.id))
        if len(contacts_not_in_group) == 0:
            contact = app.contact.create(Contact(firstname="abcd"))
        else:
            contact = random.choice(contacts_not_in_group)
        # добавляем выбранный контакт в выбранную группу
        app.contact.add_contact_in_group_by_id(contact.id, group.id)
        # получаем список контактов входящих в данную группу, после добавления контакта
        new_contacts_in_group = db.get_contacts_in_group(Group(id=group.id))
        # Проверка
        # К старому списку контактов, входящих в группу, присоединяем новый добавленный контакт
        old_contacts_in_group.append(contact)
        # Проверяем старый список с новым
        assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)
        if check_ui:
            # Проверяем новый список контактов входящих в группу, полученный из БД, со списокм, полученным из UI
            assert sorted(new_contacts_in_group, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    finally:
        pass