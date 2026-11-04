from re import findall


# подсчет слов
def count_words(text: str) -> int:
    return len(text.split())


text = input("Введите текст: ")
print(f"Количество слов: {count_words(text)}")


# подсчет слов с помощью регулярки, игнорируем знаки препиная
def count_words_clean(text: str) -> int:
    words = findall(r"\b\w+\b", text)
    return len(words)


text = "Привет, мир! Как дела?"
print(f"Слов (с пунктуацией): {count_words(text)}")
print(f"Слов (без пунктуации): {count_words_clean(text)}")
