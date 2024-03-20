# Даны 2 списка: a = [4,6,'pу','tell',78] b = [44,'hello’,56,'exept’,3]
# Выполнить следующие операции:
#     1)Сложить два списка
#     2) Добавьте число 6 на 3 позицию.
#     3)Удалите все текстовые элементы списка
#     4) Посчитайте количество элементов списка

list1 = [4, 6, 'ру', 'tell', 78]
list2 = [44, 'hello', 56, 'exept', 3]
new_list = list1 + list2
new_list.insert(2, 6)
new_list = [x for x in new_list if not isinstance(x, str)]
count = len(new_list)
print("Результат после сложения двух списков:", new_list)
print("Результат после добавления числа 6 на 3 позицию:", new_list)
print("Результат после удаления текстовых элементов списка:", new_list)
print("Количество элементов в списке:", count)
