# 1) Функция для вывода таблицы умножения для указанного числа

def mult_table(num):
    for i in range(1, num + 1):
        print(f'{num} * {i} = {num * i}')


mult_table(int(input('Введите число: ')))

