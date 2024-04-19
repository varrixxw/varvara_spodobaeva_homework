# На вход функция more_than_five(lst) получает список из целых чисел.
# Результатом работы функции должен стать новый список,
# в котором содержатся только те числа, которые больше 5 по модулю.

def more_than_five(lst):
    result = [x for x in lst if abs(x) > 5]
    return result


numbers = [3, -7, 8, 2, -6, 10]
new_numbers = more_than_five(numbers)
print(new_numbers)

