# Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить
# своё место в строю. Помогите ему это сделать. Программа получает на вход
# невозрастающую последовательность натуральных чисел, означающих рост каждого человека в
# строю. После этого вводится число X – рост Пети. Все числа во входных данных натуральные
# и не превышают 200.
# Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с
# одинаковым ростом, таким же, как у Пети, то он должен встать после них.

import random
height_of_pupils = [random.randint(145, 200) for i in range(10)]
list.sort(height_of_pupils)
print(height_of_pupils)
height = int(input('Введите рост Пети: '))
position = 0
for i in range(len(height_of_pupils)):
    if height_of_pupils[i] > height:
        index = i
        position += i
        break
    if height_of_pupils[i] == height:
        index = i + 1
        position += i + 1
        break
height_of_pupils.insert(i, height)
print(height_of_pupils)
print(f'Петя станет в строй под номером {position}')

