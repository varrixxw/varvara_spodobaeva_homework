# 12.	С клавиатуры вводится десятизначное число.
# Вывести на экран четные числа входящие в данное число. Например 1234567892  2 4 6 7 8 2

number = input("Введите десятизначное число: ")
even_numbers = [int(digit) for digit in number if int(digit) % 2 == 0]
print(even_numbers)

