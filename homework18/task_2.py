# 2) Класс «Прямоугольный треугольник»
# Класс содержит два действительных числа – стороны треугольника.
# и включает следующие методы: увеличение/уменьшение размера стороны на заданное количество процентов;
# вычисление радиуса описанной окружности, вычисление периметра, определение значений углов.

import math

class RightTriangle:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        self.hypotenuse = math.sqrt(side1**2 + side2**2)

    def increase_side(self, percent):
        self.side1 *= 1 + percent / 100
        self.side2 *= 1 + percent / 100
        self.hypotenuse = math.sqrt(self.side1**2 + self.side2**2)

    def decrease_side(self, percent):
        self.side1 *= 1 - percent / 100
        self.side2 *= 1 - percent / 100
        self.hypotenuse = math.sqrt(self.side1**2 + self.side2**2)

    def circumcircle_radius(self):
        return self.hypotenuse / 2

    def perimeter(self):
        return self.side1 + self.side2 + self.hypotenuse

    def angles(self):
        angle1 = math.degrees(math.asin(self.side1 / self.hypotenuse))
        angle2 = math.degrees(math.asin(self.side2 / self.hypotenuse))
        angle3 = 90
        return angle1, angle2, angle3


side1 = float(input("Введите длину первой стороны треугольника: "))
side2 = float(input("Введите длину второй стороны треугольника: "))

triangle = RightTriangle(side1, side2)
print("Периметр треугольника:", triangle.perimeter())
print("Радиус описанной окружности:", triangle.circumcircle_radius())
print("Значения углов:", triangle.angles())

percent_increase = float(input("Введите процент увеличения сторон треугольника: "))
triangle.increase_side(percent_increase)
print("Новый периметр после увеличения сторон на {}%:".format(percent_increase), triangle.perimeter())



