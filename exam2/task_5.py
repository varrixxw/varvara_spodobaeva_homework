# 5) Класс «Волшебник» (Wizard)
# Экземпляр класса при инициализации принимает аргументы:
# – имя;
# – рейтинг;
# – на какой возраст выглядит.
# Класс должен обеспечивать функциональность:
# – change_rating(value) – изменять рейтинг на значение value; не может стать больше 100 и
# меньше 1, изменяется только до достижения экстремального значения; при увеличении
# рейтинга уменьшается возраст на abs(value) // 10, но только до 18, дальше не уменьшается;
# при уменьшении рейтинга возраст соответственно увеличивается;
# – к экземпляру класса можно прибавить строку: (wd += string), значение рейтинга
# увеличивается на ее длину, а возраст, соответственно, уменьшается на длину // 10, условия
# изменения такие же;
# – экземпляр класса можно вызвать с аргументом-числом; возвращает значение: (аргумент
# - возраст) * рейтинг;
# __str__() – возвращает строку:
# “Wizard <name> with <rating> rating looks <age> years old”
# – экземпляры класса можно сравнивать: сначала по рейтингу, затем по возрасту, затем по
# имени по алфавиту; для этого нужно реализовать методы сравнения: <, >, <=, >=, ==, !=.

class Wizard:
    def __init__(self, name, rating, age):
        self.name = name
        self.rating = rating
        self.age = age

    def change_rating(self, value):
        if 1 <= self.rating + value <= 100:
            if value > 0:
                decrease_age = min(abs(value) // 10, self.age - 18)
                self.age -= decrease_age
            else:
                self.age += abs(value) // 10
            self.rating += value

    def __iadd__(self, string):
        self.rating += len(string)
        self.age -= len(string) // 10 if len(string) // 10 <= self.age - 18 else self.age - 18
        return self

    def __call__(self, number):
        return (number - self.age) * self.rating

    def __str__(self):
        return f"Wizard {self.name} with {self.rating} rating looks {self.age} years old"

    def __lt__(self, other):
        if self.rating != other.rating:
            return self.rating < other.rating
        elif self.age != other.age:
            return self.age < other.age
        else:
            return self.name < other.name

    def __gt__(self, other):
        if self.rating != other.rating:
            return self.rating > other.rating
        elif self.age != other.age:
            return self.age > other.age
        else:
            return self.name > other.name

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other

    def __eq__(self, other):
        return self.name == other.name and self.rating == other.rating and self.age == other.age

    def __ne__(self, other):
        return not self.__eq__(other)
# Создание экземпляров класса Wizard
wizard1 = Wizard("Гендальф", 85, 60)
wizard2 = Wizard("Саруман", 90, 70)
wizard3 = Wizard("Радагаст", 75, 50)

# Изменение рейтинга
wizard1.change_rating(10)
wizard2.change_rating(-5)

# Добавление к экземпляру класса строки
wizard3 += "Мудрый"

# Вызов экземпляра класса с числовым аргументом
result = wizard1(25)

# Вывод информации
print(wizard1)
print(wizard2)
print(wizard3)
print(result)

# Сравнение экземпляров класса
print(wizard1 < wizard2)  # True
print(wizard2 > wizard3)  # True
print(wizard1 == wizard3)  # False





