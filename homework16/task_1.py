# 1) Реализовать калькулятор с 4 методами:
# Сумма, вычитание , умножение, деление.
# Метод принимает 2 аргумента и возвращает результат.
# Невалидные данные должны быть обработаны(в классе написать проверку на валидность данных)

class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        try:
            result = num1 / num2
        except ZeroDivisionError:
            return "Ошибка: деление на ноль"
        except Exception as e:
            return f"Ошибка: {e}"
        else:
            return result

calc = Calculator()

while True:
    operator = input("Введите оператор (+, -, *, /) или 'стоп' для завершения: ")

    if operator.lower() == 'стоп':
        print("Работа калькулятора завершена.")
        break

    if operator not in ['+', '-', '*', '/']:
        print("Неверный оператор. Попробуйте еще раз.")
        continue

    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    if operator == '+':
        print("Результат:", calc.add(num1, num2))
    elif operator == '-':
        print("Результат:", calc.subtract(num1, num2))
    elif operator == '*':
        print("Результат:", calc.multiply(num1, num2))
    elif operator == '/':
        print("Результат:", calc.divide(num1, num2))

