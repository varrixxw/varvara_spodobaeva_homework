# 4) Напишите программу с классом Student, в котором есть три атрибута: name, groupNumber и age. По умолчанию name = Ivan,
# age = 18, groupNumber = 10A. Необходимо создать пять методов: getName, getAge, getGroupNumber, setNameAge,
# setGroupNumber. Метод getName нужен для получения данных об имени конкретного студента, метод getAge нужен для получения
# данных о возрасте конкретного студента, vетод setGroupNumberнужен для получения данных о номере группы конкретного
# студента. Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию, метод setGroupNumber
# позволяет изменить номер группы установленный по умолчанию. В программе необходимо создать пять экземпляров класса
# Student, установить им разные имена, возраст и номер группы.

class Student:
    def __init__(self, name="Ivan", age=18, group_number="10A"):
        self.name = name
        self.age = age
        self.group_number = group_number

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.group_number

    def setNameAge(self, name, age):
        self.name = name
        self.age = age

    def setGroupNumber(self, group_number):
        self.group_number = group_number


student1 = Student("Иван", 19, "11A")
student2 = Student("Петр", 18, "10B")
student3 = Student("Мария", 20, "12A")
student4 = Student("Сергей", 17, "9B")
student5 = Student("Екатерина", 21, "11B")


print(f"Имя: {student1.getName()}, Возраст: {student1.getAge()}, Группа: {student1.getGroupNumber()}")
print(f"Имя: {student2.getName()}, Возраст: {student2.getAge()}, Группа: {student2.getGroupNumber()}")
print(f"Имя: {student3.getName()}, Возраст: {student3.getAge()}, Группа: {student3.getGroupNumber()}")
print(f"Имя: {student4.getName()}, Возраст: {student4.getAge()}, Группа: {student4.getGroupNumber()}")
print(f"Имя: {student5.getName()}, Возраст: {student5.getAge()}, Группа: {student5.getGroupNumber()}")




