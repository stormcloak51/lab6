text = input("Введите текст: ").lower()
vowels = "аеёиоуыэюяaeiou"

count = sum(1 for char in text if char in vowels)
print(f"Количество гласных: {count}")
