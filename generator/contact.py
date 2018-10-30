from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["numder of contact", "file="])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))
    # out.write(json.dumps(test_data, default=lambda x: x.__dict__, indent=2))
