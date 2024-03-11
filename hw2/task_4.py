#  Разделить строку “Apples, Oranges, Pears, Bananas, Berries” по запятым и
# вывести на экран. Затем объединить элементы с использованием пробела,
# чтобы программа вывела “Apples Oranges Pears Bananas Berries”.

fruits = "Apples, Oranges, Pears, Bananas, Berries"
fruits_list = fruits.split(", ")
print(fruits_list)
combined_fruits = " ".join(fruits_list)
print(combined_fruits)
