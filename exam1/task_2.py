# 2.	Написать программу для вычисления значения выражений.
# Проверить правильность выполнения задания с помощью тестовых значений.

import math
a = int(input("Введите значение альфа:"))
b = int(input("Введите значение бета:"))
c = int(input("Введите значение гамма:"))
alpha = math.radians(a)
beta = math.radians(b)
gamma = math.radians(c)
y = 1/4 * (math.sin(alpha + beta - gamma) + math.sin(beta + gamma - alpha)
           + math.sin(gamma + alpha - beta) - math.sin(alpha + beta + gamma))
print(f"Значение y для α = {math.degrees(alpha)} β = {math.degrees(beta)} γ = {math.degrees(gamma)} равно: y = {y}")
