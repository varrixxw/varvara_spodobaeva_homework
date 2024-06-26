# Напишите программу, которая вычисляет процентное содержание символов G (гуанин) и C (цитозин) в введенной строке
# (программа не должна зависеть от регистра вводимых символов).
# Например, в строке "acggtgttat" процентное содержание символов G и C равно
# 4/10 ⋅ 100 = 40.0 где 4 - это количество символовG и C, а 10 -- это длина строки.

dna_sequence = input("Введите ДНК последовательность: ").upper()
gc_content = (dna_sequence.count('G') + dna_sequence.count('C')) / len(dna_sequence) * 100
print(f"Процентное содержание символов G и C: {gc_content}%")
