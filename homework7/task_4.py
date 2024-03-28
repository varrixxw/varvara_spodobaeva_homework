#  Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс
# этого элемента в списке. Если наибольших элементов несколько, выведите индекс первого из них.

list4 = [7, 15, 3, 10, 15, 2]
index_of_max = 0
for i in range(1, len(list4)):
    if list4[i] > list4[index_of_max]:
        index_of_max = i
print(list4[index_of_max], index_of_max)
