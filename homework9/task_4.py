# На вход программы подается словарь a = {1:10, 2:20, 3:30},
# необходимо получить список произведения ключа на значение.

a = {1: 10, 2: 20, 3: 30}
result = [key * value for key, value in a.items()]
print(result)

