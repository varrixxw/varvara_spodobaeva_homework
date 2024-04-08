# 14.	Напишите программу, которая принимает текст и выводит два слова:
# наиболее часто встречающееся и самое длинное.

text = input("Введите текст: ")
words = text.split()
word_counts = {word: words.count(word) for word in set(words)}
most_common_word = max(word_counts, key=word_counts.get)
longest_word = max(words, key=len)
print("Наиболее часто встречающееся слово:", most_common_word)
print("Самое длинное слово:", longest_word)
