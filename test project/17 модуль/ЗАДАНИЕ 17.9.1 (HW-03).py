# numbers = input("Введите последовательность чисел через пробел:")
# like_number = int(input("Введите любое число:"))
def is_int(str):
    str = str.replace(' ', '')
    try:
        int(str)
        return True
    except ValueError:
        return False

while True:
    try:
        numbers = input("Введите последовательность чисел через пробел:")
        if " " not in numbers:
            print("Нет пробелов")
            raise ValueError

        if not is_int(numbers):
            print("Нет чисел, либо присутствуют другие символы")
            # raise ValueError
        if len(numbers.replace(" ", ""))<2:
            # print(len(numbers))
            print("Много пробелов, мало чисел")

            raise ValueError
        else:

            print(numbers)
            break
    except ValueError:
        print('Ошибка! Введите только целые числа через пробел')
numbers = numbers.split()
list_numbers = [int(item) for item in numbers]

def merge_sort(L):
    middle = len(L) // 2
    left = merge_sort(L[:middle])
    right = merge_sort(L[middle:])
    return merge(left, right)