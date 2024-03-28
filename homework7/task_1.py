# Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.

list1 = [5, 8, 2, 10, 15, 3]
new_list = []
for i in range(len(list1) - 1):
    n = list1[i]
    i += 1
    m = list1[i]
    if m > n:
        new_list.append(m)
print(new_list)
