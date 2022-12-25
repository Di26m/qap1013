
# def get_multi(a):
#     count = 0
#     for i in range(1, a + 1):
#         if a % i == 0:
#             count +=1
#
#     return count
# print(get_multi(5))

# def multi(*nums):
#     proizv = 1
#     for i in nums:
#         proizv *= i
#     return proizv
# print(multi(2, 2, 3))
# ____________________________________________
# Сумма чисел от 1 до n (рекурсивная функция)

# def rec_fun(n):
#     if n == 1:
#         return 1
#     return n + rec_fun(n - 1)
# print(rec_fun(100))

# ____________________________________________
# # разворот строки
# def rec_str(string):
#     if len(string) == 0:
#         return ''
#     else:
#         return string[-1] + rec_str(string[:-1])
# print(rec_str('test'))
# # ---------------------------------------------
# # Задание 14.2.5
# # Дано натуральное число N. Вычислите сумму его цифр.
#
# def sum_digit(n):
#    if n < 10:
#        return n
#    else:
#        return n % 10 + sum_digit(n // 10)
#
# print(sum_digit(1234))

# a = ["asd", "bbd", "ddfa", "mcsa"]
# # print(list(map(lambda x: len(str(x)), a)))
# print(list(map(lambda x: len(x), a)))

a = ["это", "маленький", "текст", "обидно"]
print(list(map(str.upper, a)))