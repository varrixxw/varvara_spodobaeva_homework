# 6) Класс «Сотрудник компании» Worker
# Экземпляр класса при инициализации принимает аргументы:
# имя, должность и стаж работы сотрудника, метод print_info() выводит информацию о сотруднике в формате:
# «Имя: Василий Должность: Системный администратор :Стаж: 3 года» При выводе стажа нужно учитывать,
# что «года» должно заменяться на «лет» или «год» в зависимости от числа.
# worker1 = Worker("Алексей", "Программист", 17)
#  worker1.print_info()
# worker2 = Worker("Анна", "Маркетолог", 2)
# worker2.print_info()
# worker3 = Worker("Дмитрий", "Аналитик", 1)
# worker3.print_info()

class Worker:
    def __init__(self, name, position, experience):
        self.name = name
        self.position = position
        self.experience = experience

    def print_info(self):
        if self.experience % 10 == 1 and self.experience % 100 != 11:
            unit = "год"
        elif 2 <= self.experience % 10 <= 4 and (self.experience % 100 < 10 or self.experience % 100 >= 20):
            unit = "года"
        else:
            unit = "лет"

        print(f"Имя: {self.name}, Должность: {self.position}, Стаж: {self.experience} {unit}")


# Ввод данных сотрудников с использованием input()
workers = []
for i in range(3):
    name = input("Введите имя сотрудника {}: ".format(i + 1))
    position = input("Введите должность сотрудника {}: ".format(i + 1))
    experience = int(input("Введите стаж сотрудника {} в годах: ".format(i + 1)))
    worker = Worker(name, position, experience)
    workers.append(worker)


for worker in workers:
    worker.print_info()
