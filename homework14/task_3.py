# 3) В текстовом файле посчитать количество строк,
# а также для каждой отдельной строки определить
# количество в ней символов.

with open('task3.txt.py', 'r') as file:
    lines = file.readlines()
    number_of_lines = len(lines)
characters_count = [len(line.strip()) for line in lines]
print(f"Количество строк в файле: {number_of_lines}")
print("Количество символов в каждой строке:")
for i, count in enumerate(characters_count, 1):
    print(f"Строка {i}: {count}")

