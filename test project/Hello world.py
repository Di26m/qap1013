# <<<<<<< HEAD
# numbers = '1 2 3 4 5 6 7'
# n = numbers.split(' ')
# nn = '\n'.join(n)
# print(nn)
#
# for i in numbers:
#     print(i)
# все операции - деление строки по пробелам, преобразование к числам
# и приведение объекта map к типу список, можно делать в одной строке
# book = {}
# book['title'] = input('title')
# book['author'] = input('author')
# book['year'] = int(input('year'))
# print(book)
# print(type(book.values()))
# text = input("Введите текст: ")
# uniq = list(set(text))
# # uniq = set(text)
# print(len(uniq))
# # print(uniq)
# shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
# list_id_before = id(shopping_center[-1])
#
# shopping_center[-1].append("Uniqlo")
# list_id_after = id(shopping_center[-1])
#
# print( list_id_before == list_id_after,list_id_before is list_id_after   )

# n = str(1235689654)
#
# print(('3' in n) & ('7' in n))


# n = 1
# # while n ** 2 < 1000:
# #    print(n)
# #    n += 1
# #    if n>= 1000:
# #       break
# #
# # print("Количество чисел: ", n)

#
# some_var = (2,)
# if some_var is None:
#     print("NoneType")
# else:
#     print(type(some_var))

# a = "foo"
# b = "bar"
#
# print(1 and a or b)

# 13.8.12
# L = list(map(int, input().split()))
#
# print(all(L))
# L = list(map(int, input().split()))
#
# print(not any(L))

# 13.8.13
# T = [[i*j for j in range(1,11)] for i in range(1,11)]
# print((T))

# 13.8.15
# L = [int(input()) % 2 == 0 for i in range(5)]
# print( any(L))
# =======
# print('Hello World!')
# >>>>>>> origin/main
myFile = open('namefile.txt', 'w')
myFile.write('tttt')
print('zzzz', file = myFile)