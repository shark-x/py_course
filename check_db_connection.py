# import mysql.connector
#
# connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password="")
#
# try:
#     cursor = connection.cursor()
#     cursor.execute("select * from group_list")
#     for row in cursor.fetchall():
#         print(row)
# finally:
#     connection.close()


# import pymysql.cursors
#
# connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
#
# try:
#     cursor = connection.cursor()
#     cursor.execute("select * from group_list")
#     for row in cursor.fetchall():
#         print(row)
# finally:
#     connection.close()

# from fixture.db import DbFixture
#
# db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")
#
# try:
#     contacts = db.get_contact_list()
#     for contact in contacts:
#         print(contact)
#     print(len(contacts))
# finally:
#     db.destroy()

# from fixture.orm import ORMFixture
# from model.group import Group
#
# db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
#
# try:
#     li = db.get_contacts_in_group(Group(id="317"))
#     for item in li:
#         print(item)
#     print(len(li))
# finally:
#     pass #db.destroy()