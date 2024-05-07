# 1) Создайте класс Students, содержащий поля:
# фамилия и инициалы, номер группы, успеваемость (список из пяти элементов).
# Создать класс School: Добавить возможно для добавления студентов в школу
# Добавить возможность вывода фамилий и номеров групп студентов, имеющих оценки, равные только 5 или 6.
# Добавить возможность вывода учеников заданной группы
# Добавить возможность вывода учеников претендующих на автомат(средний балл >= 7)

class Student:
    def __init__(self, full_name, group_number, grades):
        self.full_name = full_name
        self.group_number = group_number
        self.grades = grades

class School:
    def __init__(self):
        self.students = []

    def add_student(self):
        full_name = input("Введите фамилию и инициалы студента: ")
        group_number = input("Введите номер группы студента: ")
        grades = []
        for i in range(5):
            grade = int(input(f"Введите оценку за предмет {i+1}: "))
            grades.append(grade)
        student = Student(full_name, group_number, grades)
        self.students.append(student)

    def high_achievers(self):
        high_achievers_list = [student.full_name for student in self.students if all(grade >= 5 for grade in student.grades)]
        return high_achievers_list

    def students_by_group(self, group_number):
        students_in_group = [student.full_name for student in self.students if student.group_number == group_number]
        return students_in_group

    def honor_students(self):
        honor_students_list = [student.full_name for student in self.students if sum(student.grades) / len(student.grades) >= 7]
        return honor_students_list


school = School()


for i in range(2):  #а
    print(f"Добавление студента {i+1}:")
    school.add_student()

print("Студенты с высокими оценками (5 или 6):", school.high_achievers())


group_number = input("Введите номер группы, чтобы получить список студентов: ")
print(f"Студенты в группе {group_number}:", school.students_by_group(group_number))

т
print("Студенты, претендующие на автомат:", school.honor_students())
