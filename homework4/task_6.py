# Пользователь вводит два числа с клавиатуры. Вывести на экран yes,
# если они отличаются друг от друга на 135,
# иначе вывести на экран No;

number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
if abs(number1 - number2) == 135:
    print("yes")
else:
    print("no")

