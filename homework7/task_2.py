# Дан список чисел. Если в нем есть два соседних элемента одного знака,
# выведите эти числа. Если соседних элементов одного знака нет — не выводите ничего.
# Если таких пар соседей несколько — выведите первую пару.

list2 = [-2, -3, 5, -1, 4, -9]
new_list = []
for i in range(len(list2)-1):
    if (list2[i] > 0 and list2[i+1] > 0) or (list2[i] < 0 and list2[i+1] < 0):
        new_list.append(list2[i])
        new_list.append(list2[i+1])
print(new_list[0], new_list[1])