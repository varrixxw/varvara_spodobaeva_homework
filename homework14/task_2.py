# 2) Создать текстовый файл, записать в него построчно
# данные, которые вводит пользователь. Окончанием ввода
# пусть служит пустая строка.

with open('task2.txt.py', 'r') as file:
    while True:
        user_input = input("Введите строку (пустая строка для завершения): ")
        if user_input == "":
            break
        else:
            file.write(user_input + "\n")
