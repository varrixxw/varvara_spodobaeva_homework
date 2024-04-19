 # Напишите программу, которая подключает модуль math и, используя значение числа piπ
 # из этого модуля, находит для переданного ей на стандартный ввод радиуса круга периметр этого круга
 # и выводит его на стандартный вывод.

import math


def calculate_circle_perimeter(radius):
    perimeter = 2 * math.pi * radius
    return perimeter


radius = float(input("Введите радиус круга: "))
result = calculate_circle_perimeter(radius)
print(f"Периметр круга: {result}")
