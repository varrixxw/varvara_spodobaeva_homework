# Простейший калькулятор с введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: "Деление на ноль"
# Ноль использовать в качестве завершения программы (сделать как отдельную

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Деление на ноль"
    else:
        return a / b


while True:
    operation = input("Выберите операцию (+, -, *, /) или введите 0 для выхода: ")
    if operation == '0':
        break
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    if operation == '+':
        print(add(num1, num2))
    elif operation == '-':
        print(subtract(num1, num2))
    elif operation == '*':
        print(multiply(num1, num2))
    elif operation == '/':
        print(divide(num1, num2))
    else:
        print("Неверная операция")
