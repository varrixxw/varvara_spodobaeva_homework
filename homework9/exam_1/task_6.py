# 6.	Вам передан массив чисел.
# Известно, что каждое число в этом массиве имеет пару, кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5

numbers = [1, 5, 2, 9, 2, 9, 1]
unique_number = 0
for num in numbers:
    unique_number ^= num
print(unique_number)
