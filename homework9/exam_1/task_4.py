# 4.	В строке “Иван Иванов” поменяйте местами слова.
# Может быть предоставлена любая строка с именем и фамилией. 	например
# “Петр Иванов” => “Иванов Петр”

name = "Иван Иванов"
name_list = name.split()
reversed_name = name_list[1] + " " + name_list[0]
print(reversed_name)
