# Дан список list=[15,48,'hello',6,19,'world’].
# Все числа этого списка проверить на чётность. Если число чётное,
# то посчитать сумму его цифр. - результат число
# Если нечётное, то заменить его на 1 в списке. - результат список
# Все слова: посчитать количество гласных и согласных.
# Вывести всё на экран.

def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))
def count_vowels_consonants(word):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    num_vowels = sum(1 for char in word if char in vowels)
    num_consonants = sum(1 for char in word if char in consonants)
    return num_vowels, num_consonants
my_list = [15, 48, 'hello', 6, 19, 'world']
for i in range(len(my_list)):
    if isinstance(my_list[i], int):
        if my_list[i] % 2 == 0:
            my_list[i] = sum_of_digits(my_list[i])
        else:
            my_list[i] = 1
for item in my_list:
    if isinstance(item, str):
        num_vowels, num_consonants = count_vowels_consonants(item)
        print(f'Слово "{item}" содержит {num_vowels} гласных и {num_consonants} согласных.')
print("Обновленный список:", my_list)


