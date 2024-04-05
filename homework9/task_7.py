# Создать множество. Создать неизменяемое множество. Выполнить операцию объединения
# созданных множеств. Выполнить операцию пересечения созданных множеств.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
frozenset1 = frozenset({1, 2, 3})
union_set = set1.union(set2)
print(union_set)
intersection_set = set1.intersection(set2)
print(intersection_set)
