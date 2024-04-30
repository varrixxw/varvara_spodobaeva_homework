# 2) Вы идете в путешествие, надо подсчитать сколько у денег у каждого студента.
# Класс студен описан следующим образом:
# class Student:
#     def __init__(self, name, money):
#        self.name = name
#        self.money = money

class Student:
    def __init__(self, name, money):
        self.name = name
        self.money = money

def calculate_total_money(students):
    total_money = sum(student.money for student in students)
    return total_money


num_students = int(input("Введите количество студентов: "))


students = []
for i in range(num_students):
    name = input(f"Введите имя студента {i+1}: ")
    money = int(input(f"Введите количество денег у студента {i+1}: "))
    students.append(Student(name, money))

# Print information about each student and the total amount of money
for student in students:
    print(f"{student.name}: {student.money} money")

total_money = calculate_total_money(students)
print(f"Общая сумма денег у всех студентов: {total_money}")




