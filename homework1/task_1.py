# Необходимо написать программу, которая требует у пользователя ввести
# два целых числа, строку и одно дробное число, далее выводит на экран
# строку и сумму двух целых и дробного числа.

int_number1 = int(input('Введите первое целое число'))
int_number2 = int(input('Введите второе целое число'))
str_name1 = input('Введите строку')
float_number1 = float(input('Введите дробное число'))
number_sum = int_number1 + int_number2 + float_number1
print(str_name1)
print(number_sum)
