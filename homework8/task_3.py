# Из передачи “Здоровье” Аня узнала, что рекомендуется спать хотя бы A часов в сутки, но пересыпать
# тоже вредно и не стоит спать более B часов. Сейчас Аня спит H часов в сутки. Если режим
# сна Ани удовлетворяет рекомендациям передачи “Здоровье”, выведите “Это нормально”.
# Если Аня спит менее A часов, выведите “Недосып”, если же более B часов, то выведите
# “Пересып”. Получаемое число A всегда меньше либо равно B.

A = int(input('Введите рекомендуемое количество часов: '))
B = int(input('Введите сколько часов не рекомендуется спать: '))
H = int(input('Введите сколько часов спит Аня: '))
if H < A:
    print("Недосып")
elif H <= B and H >= A:
    print("Это нормально")
elif H > B:
    print("Пересып")


