#  Казино. Компьютер генерирует числа от 1 до 10 и от 1 до двух соответственно.
# Цифры от 1 до 10 отвечают за номера, а от 1 до 2 за цвета(1-красный, 2-черный).
# Пользователю дается 5 попыток угадать номер и цвет(Пример. Вводим с клавиатуры: 3 красный)
# В случае неудачи, вывести на экран правильную комбинацию.

import random
number = random.randint(1, 10)
color = random.randint(1, 2)
colors = {1: 'красный', 2: 'черный'}
attempts = 5
while attempts > 0:
    guess = input("Угадайте номер и цвет (например, '3 красный'): ").split()
    if len(guess) != 2:
        print("Неверно. Попробуйте снова.")
        continue
    guess_number = guess[0]
    guess_color = guess[1].lower()
    if not guess_number.isdigit():
        print("Неверно. Попробуйте снова.")
        continue
    guess_number = int(guess_number)
    if guess_number == number and guess_color == colors[color]:
        print("Поздравляем! Вы угадали номер и цвет.")
        break
    else:
        print("Неправильно. Правильная комбинация: {} {}".format(number, colors[color]))
        attempts -= 1
if attempts == 0:
    print("Вы проиграли. Правильная комбинация: {} {}".format(number, colors[color]))

