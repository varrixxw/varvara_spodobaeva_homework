# 1) Даны два кортежа. Требуется объединить их между собой.

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (6, 7, 8, 9, 10)
combined_tuple = tuple1 + tuple2
print(combined_tuple)

# 2) В кортеже целых чисел найдите максимальный и минимальный элементы,
# а также осуществите их обмен.

numbers = (5, 3, 8, 2, 10)
max_number = max(numbers)
min_number = min(numbers)
print(f"Максимальный элемент: {max_number}, Минимальный элемент: {min_number}")
numbers = list(numbers)
max_index = numbers.index(max_number)
min_index = numbers.index(min_number)
numbers[max_index], numbers[min_index] = numbers[min_index], numbers[max_index]
numbers = tuple(numbers)
print(f"Кортеж после обмена: {numbers}")

# 3) В список, сгенерированный случайным образом, добавить введенный
# пользователем элемент.

import random
random_list = [random.randint(1, 10) for _ in range(5)]
element = int(input("Введите элемент для добавления в список: "))
random_list.append(element)
print(random_list)

# 4) В список, сгенерированный случайным образом, добавить введенный
# пользователем элемент на указанную позицию.

position = int(input("Введите позицию для добавления элемента: "))
element4 = int(input("Введите элемент для добавления в список: "))
random_list.insert(position, element4)
print(random_list)

# 5) Имеются два списка, сгенерированные случайным образом. Добавьте в
# конец первого списка все элементы второго списка.

import random
list5 = [random.randint(1, 10) for i in range(5)]
list6 = [random.randint(1, 10) for i in range(5)]
list5.extend(list6)
print(list5)

# 6) Из заранее сформированного списка следует удалить элемент, введенный
# пользователем.

list7 = ["apple", "banana", "cherry", "date", "fig"]
print("Исходный список:",list7)
element = input("Введите элемент для удаления из списка: ")
if element in list7:
    list7.remove(element)
    print("Список после удаления:", list7)
else:
    print("Введенный элемент отсутствует в списке.")

# 7) Из исходного списка следует удалить элемент, позицию которого указал пользователь.

list8 = [5, 8, 12, 6, 9, 3, 7]
print("Исходный список:", list8)
position = int(input("Введите позицию элемента для удаления: "))
if 0 <= position < len(list8):
    del list8[position]
    print("Список после удаления:", list8)
else:
    print("Введенной позиции нет.")

# 8) В кортеже целых чисел вычислите произведение отрицательных
# элементов, имеющих нечетные индексы.

import random
x = tuple(random.randint(-50, 10) for i in range(10))
print(x)
number = 1
for i in range(1, len(x), 2):
    if x[i] < 0:
        number *= x[i]
        print(x[i])
print(number)

# 9) Заполните один кортеж десятью случайными целыми числами от 0 до 5
# включительно. Также заполните второй кортеж числами от -5 до 0.
# Объедините два кортежа с помощью оператора +, создав тем самым третий
# кортеж. С помощью метода кортежа count() определите в нем количество
# нулей. Выведите на экран третий кортеж и количество нулей в нем.

import random
tuple9 = tuple(random.randint(0, 5) for i in range(10))
tuple10 = tuple(random.randint(-5, 0) for i in range(10))
combined_tuple = tuple9 + tuple10
zero_count = combined_tuple.count(0)
print(f"Объединенный кортеж: {combined_tuple}, Количество нулей: {zero_count}")

# 10) Вывести данные кортежа без скобок, через запятую. Обязательно:
# элементы кортежа – строки.

tuple11 = ("apple", "banana", "orange", "grape")
print(", ".join(tuple11))

# 11) Сгенерируйте 2 кортежа случайными числами в диапазоне от 10-90.
# Количество элементов в кортеже 10. Определить: 1) Сумма элементов какого
# из кортежей больше и вывести соответствующее сообщение на экран (
# Сумма больше в кортеже - ..) 2) Вывести на экран порядковые номера
# минимальных элементов этих кортежей

tuple12 = tuple(random.randint(10, 90) for i in range(10))
tuple13 = tuple(random.randint(10, 90) for i in range(10))
sum1 = sum(tuple12)
sum2 = sum(tuple13)
if sum1 > sum2:
    print("Сумма больше в кортеже 1")
elif sum2 > sum1:
    print("Сумма больше в кортеже 2")
else:
    print("Суммы равны")
min_index1 = [i for i, v in enumerate(tuple12) if v == min(tuple12)]
min_index2 = [i for i, v in enumerate(tuple13) if v == min(tuple13)]
print(f"Порядковые номера минимальных элементов кортежа 1: {min_index1}, кортежа 2: {min_index2}")
