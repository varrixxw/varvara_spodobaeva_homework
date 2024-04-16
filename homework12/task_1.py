# 1)Создайте функцию для определения наибольшего числа

import random

def max_number(count):
    numbers = [random.randint(1, 100) for _ in range(count)]
    print(f"Случайные числа: {numbers}")
    return max(numbers)

result = max_number(10)
print(f"Наибольшее число: {result}")





