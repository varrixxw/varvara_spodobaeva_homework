# Задача Есть Помидор со следующими характеристиками:Индекс Стадия зрелости(стадии: Отсутствует, Цветение, Зеленый, Красный)
# Помидор может:Расти (переходить на следующую стадию созревания)Предоставлять информацию о своей зрелости
# Есть Куст с помидорами, который:Содержит список томатов, которые на ней растут И может:
# Расти вместе с томатами Предоставлять информацию о зрелости всех томатовПредоставлять урожай
# И также есть Садовник, который имеет:Имя Растение, за которым он ухаживает И может:
# Ухаживать за растением Собирать с него урожай Задание: Класс TomatoСоздайте класс Tomato
# Создайте статический атрибут states, который будет содержать все стадии созревания помидора
# Создайте метод __init__(), внутри которого будут определены два приватных атрибута: 1) _index - передается параметром
# и 2) _state - принимает первое значение из словаря states
# Создайте метод grow(), который будет переводить томат на следующую стадию созревания
# Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг последней стадии созревания)
# Класс TomatoBush
# Создайте класс TomatoBush
# Определите метод __init__(), который будет принимать в качестве параметра количество томатов и на его основе будет
# создавать список объектов класса Tomato. Данный список будет храниться внутри атрибута tomatoes.
# Создайте метод grow_all(), который будет переводить все объекты из списка томатов на следующий этап созревания
# Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из списка стали спелыми
# Создайте метод give_away_all(), который будет чистить список томатов после сбора урожая
# Класс Gardener
# Создайте класс Gardener
# Создайте метод __init__(), внутри которого будут определены два атрибута: 1) name - передается параметром, является
# публичным и 2) _plant - принимает объект класса TomatoBush, является приватным
# Создайте метод work(), который заставляет садовника работать, что позволяет растению становиться более зрелым
# Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все - садовник собирает урожай.
# Если нет - метод печатает предупреждение.Создайте статический метод knowledge_base(), который выведет в консоль
# справку по садоводству.
# Тесты (main) Вызовите справку по садоводству Создайте объекты классов TomatoBush и Gardener
# Используя объект класса Gardener, поухаживайте за кустом с помидорами Попробуйте собрать урожай
# Если томаты еще не дозрели, продолжайте ухаживать за ними Соберите урожай


class Tomato:
    states = ["Отсутствует", "Цветение", "Зеленый", "Красный"]

    def __init__(self, index):
        self._index = index
        self._state = Tomato.states[0]

    def grow(self):
        current_index = Tomato.states.index(self._state)
        if current_index < len(Tomato.states) - 1:
            self._state = Tomato.states[current_index + 1]

    def is_ripe(self):
        return self._state == Tomato.states[-1]

class TomatoBush:
    def __init__(self, tomato_count):
        self.tomatoes = [Tomato(i) for i in range(1, tomato_count + 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Урожай собран!")
        else:
            print("Помидоры еще не созрели.")

    @staticmethod
    def knowledge_base():
        print("Советы по садоводству:")
        print("- Поливайте помидоры регулярно, но не переусердствуйте.")
        print("- Обеспечьте помидорам достаточное количество солнечного света.")
        print("- Подкармливайте помидоры удобрениями для улучшения роста.")
        print("- Убирайте сорняки вокруг помидоров, чтобы они не отнимали питательные вещества.")

# Тесты
Gardener.knowledge_base()

tomato_bush = TomatoBush(5)
gardener = Gardener("Джон", tomato_bush)

gardener.work()
gardener.harvest()

while not tomato_bush.all_are_ripe():
    gardener.work()

gardener.harvest()


