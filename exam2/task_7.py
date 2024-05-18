# 7) Класс ПЕРСОНА, экземпляр класса инициализируется аргументами фамилия, дата
# рождения и содержит методы, позволяющие вывести информацию о персоне, а также определить ее возраст.
# Дочерние классы: АБИТУРИЕНТ (фамилия, дата рождения, факультет),
# СТУДЕНТ(фамилия, дата рождения, факультет, курс), ПРЕПОДАВАТЕЛЬ
# (фамилия, дата рождения, факультет, должность, стаж), содержат свои методы вывода информации.
# Создайте список из n персон, выведите полную информацию из базы, а также
# организуйте поиск персон, чей возраст попадает в заданный диапазон.

import datetime


class Person:
    def __init__(self, last_name, dob):
        self.last_name = last_name
        self.dob = dob

    def info(self):
        print(f"Person: {self.last_name}, Date of Birth: {self.dob}")

    def age(self):
        today = datetime.date.today()
        age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return age


class Applicant(Person):
    def __init__(self, last_name, dob, faculty):
        super().__init__(last_name, dob)
        self.faculty = faculty

    def info(self):
        super().info()
        print(f"Faculty: {self.faculty}")


class Student(Person):
    def __init__(self, last_name, dob, faculty, course):
        super().__init__(last_name, dob)
        self.faculty = faculty
        self.course = course

    def info(self):
        super().info()
        print(f"Faculty: {self.faculty}, Course: {self.course}")


class Teacher(Person):
    def __init__(self, last_name, dob, faculty, position, experience):
        super().__init__(last_name, dob)
        self.faculty = faculty
        self.position = position
        self.experience = experience

    def info(self):
        super().info()
        print(f"Faculty: {self.faculty}, Position: {self.position}, Experience: {self.experience} years")


# Создание списка персон
persons = []


num_persons = int(input("Введите количество персон: "))
for _ in range(num_persons):
    person_type = input("Введите тип персоны (Applicant, Student, Teacher): ")
    last_name = input("Введите фамилию: ")
    dob = input("Введите дату рождения в формате ГГГГ-ММ-ДД: ")

    if person_type == "Applicant":
        faculty = input("Введите факультет: ")
        persons.append(Applicant(last_name, datetime.datetime.strptime(dob, "%Y-%m-%d").date(), faculty))
    elif person_type == "Student":
        faculty = input("Введите факультет: ")
        course = int(input("Введите курс: "))
        persons.append(Student(last_name, datetime.datetime.strptime(dob, "%Y-%m-%d").date(), faculty, course))
    elif person_type == "Teacher":
        faculty = input("Введите факультет: ")
        position = input("Введите должность: ")
        experience = int(input("Введите опыт работы (в годах): "))
        persons.append(
            Teacher(last_name, datetime.datetime.strptime(dob, "%Y-%m-%d").date(), faculty, position, experience))

# Вывод информации о каждой персоне
for person in persons:
    person.info()



def search_persons_by_age(persons_list, min_age, max_age):
    result = []
    for person in persons_list:
        if min_age <= person.age() <= max_age:
            result.append(person)
    return result



min_age = int(input("Введите минимальный возраст для поиска: "))
max_age = int(input("Введите максимальный возраст для поиска: "))
result_persons = search_persons_by_age(persons, min_age, max_age)

print("\nPersons in the age range of", min_age, "to", max_age, "years:")
for person in result_persons:
    person.info()

