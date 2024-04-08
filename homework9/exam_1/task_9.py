# 9.Дана строка [“hello my friend”, “my name is”, “house”, “cat”, “dog”].
# В новый список добавить элементы, которые содержат пробел.

string = ["hello my friend", "my name is", "house", "cat", "dog"]
new_list = [string for string in string if " " in string]
print(new_list)



