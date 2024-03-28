# В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент
# этого списка.

list6 = [-5, -3, 8, -2, 10, 15, 3, 9, 200, 909, -1099]
min_index = list6.index(min(list6))
max_index = list6.index(max(list6))
list6[min_index], list6[max_index] = list6[max_index], list6[min_index]
print(list6)

