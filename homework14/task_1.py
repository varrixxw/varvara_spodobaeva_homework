# 1) Файл содержит числа и буквы. Каждый записан в
# отдельной строке. Нужно считать содержимое в список
# так, чтобы сначала шли числа по возрастанию, а потом
# слова по возрастанию их длины. (из класса)

with open('task_hw14.txt.py', 'r') as file:
    content = file.readlines()
numbers = []
words = []
for item in content:
    item = item.strip()
    if item.isdigit():
        numbers.append(int(item))
    else:
        words.append(item)
sorted_numbers = sorted(numbers)
sorted_words = sorted(words, key=lambda x: len(x))
result = sorted_numbers + sorted_words
print(result)

