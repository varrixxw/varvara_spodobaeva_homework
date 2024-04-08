# 13.	Необходимо удалить пустые строки из списка строк.
# Пример списка: [‘1’, ‘2’,  ‘3’ , ‘4’ ,’hello’, ‘’, ‘good’ , ‘’, ‘’, ‘5’, ‘6’, ‘7’]

strings = ['1', '2', '3', '4', 'hello', '', 'good', '', '', '5', '6', '7']
non_empty_strings = [string for string in strings if string.strip()]
print(non_empty_strings)
