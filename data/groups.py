from model.group import Group


test_data = [Group(name="name1", header="header1", footer="footer1"),
            Group(name="name2", header="header2", footer="footer2")
            ]


# def random_string(prefix, maxlen):
#     symbols = string.ascii_letters + string.digits  # + " "*10
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
#
# test_data = [Group(name="", header="", footer="")]+[
#         Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 15))
#         for i in range(5)
#     ]
#
# # test_data = [Group(name=name, header=header, footer=footer)
# #              for name in ["", random_string("name", 10)]
# #              for header in ["", random_string("header", 10)]
# #              for footer in ["", random_string("footer", 10)]
# #              ]