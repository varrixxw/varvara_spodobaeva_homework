# Вычислить сумму цифр случайного трёхзначного числа (тут необходимо
# применить работу со строками)

import random
number = random.randint(100, 999)
print(number)
number_str = str(number)
sum_number = int(number_str[0]) + int(number_str[1]) + int(number_str[2])
print(sum_number)
