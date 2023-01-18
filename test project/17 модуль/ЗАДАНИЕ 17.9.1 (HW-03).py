# для проверки, что введены числа
def is_int(str):
    str = str.replace(' ', '')
    try:
        int(str)
        return True
    except ValueError:
        return False
# Заставляем пользователя сделать правильный ввод
while True:
    try:
        numbers = input("Введите последовательность чисел через пробел:")
        if " " not in numbers:
            print("Нет пробелов")
            raise ValueError

        if not is_int(numbers):
            print("Нет чисел, либо присутствуют другие символы")

        if len(numbers.replace(" ", ""))<2:
            print("Много пробелов, мало чисел")
            raise ValueError

        else:
            print(numbers)
            break
    except ValueError:
        print('Ошибка! Введите только целые числа через пробел')

while True:
    try:
        like_number = int(input("Введите любое число:"))
        break
    except ValueError:
        print('Ошибка! Введите целое число')

# Преобразование введённой последовательности в список
numbers = numbers.split()
list_numbers = [int(item) for item in numbers]

# Сортировка списка по возрастанию элементов в нем
def merge_sort(L):
    if len(L) < 2:  # если кусок массива равен 2,
        return L[:]  # выходим из рекурсии
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result

list_numbers = merge_sort(list_numbers)

# Установка позиции элемента
def binary_search(array, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return 'Число выходит за диапазон списка, введите меньшее число.'

print(f'Отсортированный по возрастанию список: {list_numbers}')

#Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу.

if not binary_search(list_numbers, like_number, 0, len(list_numbers)):
    rI = min(list_numbers, key=lambda x: (abs(x - like_number), x))
    ind = list_numbers.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < like_number:
        print(f'''В списке нет введенного элемента 
Ближайший меньший элемент: {rI}, его индекс: {ind}
Ближайший больший элемент: {list_numbers[max_ind]} его индекс: {max_ind}''')
    elif min_ind < 0:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {rI}, его индекс: {list_numbers.index(rI)}
В списке нет меньшего элемента''')
    elif rI > like_number:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {rI}, его индекс: {list_numbers.index(rI)}
Ближайший меньший элемент: {list_numbers[min_ind]} его индекс: {min_ind}''')
    elif list_numbers.index(rI) == 0:
        print(f'Индекс введенного элемента: {list_numbers.index(rI)}')
else:
    print(f'Индекс введенного элемента: {binary_search(list_numbers, like_number, 0, len(list_numbers))}')