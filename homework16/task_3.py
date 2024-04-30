# 3) Задача на декоратор
# метод sum(a, b) принимает 2 числа и возвращает их сумму.
# Написать декоратор, который возвращает ошибку
# если переданы не числовые параметры(например строка)
# пример:
# @validate_int_parameters
# def sum(a,b)`
# sum(3, "1") => ошибка
# sum(4, 2) = > 6

def validate_int_parameters(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError("Ошибка")
        return func(*args)
    return wrapper

@validate_int_parameters
def sum(a, b):
    return a + b


try:
    a = int(input("Введите первое целое число: "))
    b = int(input("Введите второе целое число: "))
    print(sum(a, b))
except ValueError as e:
    print("Ошибка:", e)



