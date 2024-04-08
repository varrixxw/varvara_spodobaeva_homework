# 1.	Используя стандартныеарифметические операции представьте
# самое большое целое число из цифр 4, 4, 4 и приведите его значение.

numbers = ['4', '4', '4']
numbers.sort(reverse=True)
biggest_number = int(''.join(numbers))
print(biggest_number)
