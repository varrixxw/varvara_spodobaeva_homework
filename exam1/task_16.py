# Дезоксирибонуклеиновая кислота (ДНК) представляет собой
# химическое вещество, находящееся в ядре клеток и несущее
# «инструкции» по развитию и функционированию живых организмов.
# В цепочках ДНК символы «А» и «Т» дополняют друг друга, как «С» и
# «G».Вам нужно вернуть другую дополнительную сторону. Нить
# ДНК никогда не бывает пустой или ДНК вообще не существует.
# Пример: (ввод --> вывод)
#
# “АТТGС" --> "ТААСG"
# “GТАТ" --> "САТА"

dna = input("Введите ДНК: ")
complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
dna_list = list(dna)
for i in range(len(dna_list)):
    dna_list[i] = complement_dict[dna_list[i]]
complement_dna = ''.join(dna_list)
print("Дополнительная сторона ДНК:", complement_dna)
