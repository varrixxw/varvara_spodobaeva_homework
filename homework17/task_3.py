# 3) Создать 4 фрукта. Апельсин, яблоко, мандарин, банан У всех фруктов есть сорт, список витаминов, цена, имя
# У апельсина, мандарина, банана есть метод очистить У яблока метод порезать У банана есть характеристика: кол-во калия
# Создать 4 объекта фрукта и использовать все доступные методы и характеристики
# При вызове метода очистить, должно писаться имя фрукта
# Например:
# `apple = Apple("sort", [a,b,c], 120, "apple")`
# `apple.clear()`
#
# `>>"apple очищен"`

class Fruit:
    def __init__(self, sort, vitamins, price, name):
        self.sort = sort
        self.vitamins = vitamins
        self.price = price
        self.name = name

    def clear(self):
        return f"Сорт: {self.sort}, Витамины: {', '.join(self.vitamins)}, Цена: {self.price}, Имя: {self.name} - очищен"

class Orange(Fruit):
    def __init__(self, sort, vitamins, price, name):
        super().__init__(sort, vitamins, price, name)

    def clear(self):
        return f"Сорт: {self.sort}, Витамины: {', '.join(self.vitamins)}, Цена: {self.price}, Имя: {self.name} - очищен"

class Apple(Fruit):
    def __init__(self, sort, vitamins, price, name):
        super().__init__(sort, vitamins, price, name)

    def cut(self):
        return f"Сорт: {self.sort}, Витамины: {', '.join(self.vitamins)}, Цена: {self.price}, Имя: {self.name} - порезан"

class Mandarin(Fruit):
    def __init__(self, sort, vitamins, price, name):
        super().__init__(sort, vitamins, price, name)

class Banana(Fruit):
    def __init__(self, sort, vitamins, price, name, potassium):
        super().__init__(sort, vitamins, price, name)
        self.potassium = potassium

    def clear(self):
        return f"Сорт: {self.sort}, Витамины: {', '.join(self.vitamins)}, Цена: {self.price}, Имя: {self.name} - очищен"


orange = Orange("Valencia", ["Витамин C", "Витамин A"], 50, "Апельсин")
print(orange.clear())

apple = Apple("Granny Smith", ["Витамин C", "Витамин K"], 60, "Яблоко")
print(apple.cut())

mandarin = Mandarin("Clementine", ["Витамин C", "Витамин B"], 40, "Мандарин")

banana = Banana("Cavendish", ["Витамин B6", "Витамин C"], 30, "Банан", "200мг")
print(banana.clear())
