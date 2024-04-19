# 3) Написать 12 функций по переводу:1. Дюймы в сантиметры 2. Сантиметры в дюймы 3. Мили в километры
# 4. Километры в мили 5. Фунты в килограммы 6. Килограммы в фунты 7. Унции в граммы 8. Граммы в унции
# 9. Галлон в литры 10. Литры в галлоны 11. Пинты в литры 12. Литры в пинты

# 1. Дюймы в сантиметры
def inches_to_centimeters(inch):
    inches = float(input("Введите значение в дюймах: "))
    centimeters = inches * 2.54
    print(f"{inches} дюймов = {centimeters} сантиметров")

# 2. Сантиметры в дюймы


def centimeters_to_inches(cm):
    centimeters = float(input("Введите значение в сантиметрах: "))
    inches = centimeters / 2.54
    print(f"{centimeters} сантиметров = {inches} дюймов")

# 3. Мили в километры


def miles_to_kilometers(mil):
    miles = float(input("Введите значение в милях: "))
    kilometers = miles * 1.60934
    print(f"{miles} миль = {kilometers} километров")

# 4. Километры в мили


def kilometers_to_miles(km):
    kilometers = float(input("Введите значение в километрах: "))
    miles = kilometers / 1.60934
    print(f"{kilometers} километров = {miles} миль")

# 5. Фунты в килограммы


def pounds_to_kilograms(pound):
    pounds = float(input("Введите значение в фунтах: "))
    kilograms = pounds * 0.453592
    print(f"{pounds} фунтов = {kilograms} килограмм")

# 6. Килограммы в фунты


def kilograms_to_pounds(kl):
    kilograms = float(input("Введите значение в килограммах: "))
    pounds = kilograms / 0.453592
    print(f"{kilograms} килограмм = {pounds} фунтов")

# 7. Унции в граммы


def ounces_to_grams(ounce):
    ounces = float(input("Введите значение в унциях: "))
    grams = ounces * 28.3495
    print(f"{ounces} унций = {grams} грамм")

# 8. Граммы в унции


def grams_to_ounces(gr):
    grams = float(input("Введите значение в граммах: "))
    ounces = grams / 28.3495
    print(f"{grams} грамм = {ounces} унций")

# 9. Галлон в литры


def gallons_to_liters(gallon):
    gallons = float(input("Введите значение в галлонах: "))
    liters = gallons * 3.78541
    print(f"{gallons} галлонов = {liters} литров")

# 10. Литры в галлоны


def liters_to_gallons(lit):
    liters = float(input("Введите значение в литрах: "))
    gallons = liters / 3.78541
    print(f"{liters} литров = {gallons} галлонов")

# 11. Пинты в литры


def pints_to_liters(pints):
    pints = float(input("Введите значение в пинтах: "))
    liters = pints * 0.473176
    print(f"{pints} пинт = {liters} литров")

# 12. Литры в пинты


def liters_to_pints(lit):
    liters = float(input("Введите значение в литрах: "))
    pints = liters / 0.473176
    print(f"{liters} литров = {pints} пинт")




