 # Вычислить сумму цифр случайного трёхзначного числа.

from random import randint
random_number = randint(10, 999)
print(random_number)
a = random_number // 100
b = (random_number // 10) % 10
c = random_number % 10
print(a + b + c)
