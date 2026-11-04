from collections import Counter
from re import findall

text = input("Введите текст: ")
words = findall(r"\b\w+\b", text.lower())
# возвращает топ-10 самых часто встречающих слов
top_words = Counter(words).most_common(10)

for word, count in top_words:
    print(f"{word}: {count}")
