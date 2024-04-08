# 7.	Дан список [student1, student2, student3]
# с помощью цикла for добавить к каждому элементу списка слово “_good”. Вывести на экран.

list7 = ["student1", "student2", "student3"]
for i in range(len(list7)):
    list7[i] += "_good"
print(list7)
