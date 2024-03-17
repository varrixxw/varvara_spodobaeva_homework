# Напишите программу, которая выполняет сравнение двух переменных.

number1 = float(input('Введите 1 переменную'))
number2 = float(input('Введите 2 переменную'))
if number1 > number2:
    print(number1,'Переменная 1 больше')
elif number2 > number1:
    print(number2, 'Переменная 2 больше')
else:
    print('Переменная 1 равно переменная 2')
