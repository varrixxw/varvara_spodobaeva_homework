# Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число - кол-во нечётных цифр.
# Строка - количество букв.
# Сделать проверку со всеми этими

def analyze_data(data):
    if isinstance(data, tuple):
        return sum(len(word) for word in data)
    elif isinstance(data, list):
        letters_count = sum(len(word) for word in data if isinstance(word, str))
        numbers_count = sum(1 for item in data if isinstance(item, int))
        odd_numbers_count = sum(1 for item in data if isinstance(item, int) and item % 2 != 0)
        return letters_count, numbers_count, odd_numbers_count
    elif isinstance(data, int):
        return sum(1 for digit in str(data) if int(digit) % 2 != 0)
    elif isinstance(data, str):
        return sum(1 for char in data if char.isalpha())
    else:
        return "Неподдерживаемый тип данных"
    

