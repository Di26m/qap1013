# myFile = open('namefile.txt', 'w')
# myFile.write('tttt')
# print('zzzz', file = myFile)

# with open('namefile.txt', 'a') as somefile:
#     somefile.write('\nproverka')
# with open('namefile.txt', 'r') as somefile:
#     print(somefile.read())


# with open('namefile.txt', 'a+') as somefile:
#     somefile.write('\nproverka')

# with open('17-4.txt') as f:
#     a = f.readlines()
#     b = [int(x) for x in a]
#     # b = list(map(int, a))
#     print(b)

# with open('17-4.txt') as f:
#     s = f.readlines()
#     a = list(map(int, s))
#     res = []
#     for i in a:
#         if str(i).count('0') >= 2 and i % 7 == 0:
#             res.append(i)
# print(max(res), len(res))

# # Посчитать количество слов в файле
# # --------------------------------
# file = open('textpython.txt', encoding='utf-8')
# data = file.read()
# words = data.split()
# print(len(words))

# JSON
# # --------------------------------
import json
# data = {
#     'name': 'Ivan',
#     'age': 26,
#     'city': 'Saratov',
#     'childres': None
# }
#
# with open('data_file.json', 'w') as f:
#     json.dump(data, f)

with open('data_file.json') as f:
    data = json.load(f)
    print(data)