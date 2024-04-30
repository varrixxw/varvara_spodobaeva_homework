# 2) Создайте функцию, которая принимает на вход список словарей и сохраняет его в CSV файл.
# Каждый словарь представляет собой строку данных, а ключи словарей - названия столбцов.

import csv

lines = [
    {'fruit': 'orange', 'cost': 5, 'color': 'orange'},
    {'fruit': 'apple', 'cost': 9, 'color': 'green'},
    {'fruit': 'pineapple', 'cost': 19, 'color': 'yellow'},
]

def save_to_csv(lines):
    with open('task2.csv.py', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(lines[0].keys())
        for i in lines:
            writer.writerow(i.values())

save_to_csv(lines)
