# Дана следующая функция y = f(x). y = 2x – 10, если x > 0, y = 0, если x = 0, y = 2 *|x| - 1, если x < 0
# Примечание: для нахождения модуля используйте встроенную функцию abs(x)

def f(x):
    if x > 0:
        return 2*x - 10
    elif x == 0:
        return 0
    else:
        return 2*abs(x) - 1
x_values = [3, 0, -2]
for x in x_values:
    print(f"При x = {x}, y = f({x}) = {f(x)}")

