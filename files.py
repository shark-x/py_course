import json

with open("d:/test/test1/test.json") as f:
    try:
        result = json.load(f)
    except json.decoder.JSONDecodeError as ex:
        print(ex)
        result = {}

print(result)


# f = open("d:/test/test1/test.json")
# try:
#     result = json.load(f)
# except json.decoder.JSONDecodeError as ex:
#     print(ex)
#     result = {}
# finally:
#     f.close()
#
# print(result)
