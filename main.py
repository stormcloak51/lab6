from re import sub


# функция для проверки слвоа-палиндром
def is_palindrome(text: str) -> bool:
    # очищает текст (оставляет только буквы и цифры)
    cleaned = sub(r"[^\w]", "", text.lower())
    return cleaned == cleaned[::-1]


tests = [
    "А роза упала на лапу Азора",
    "Madam, I'm Adam",
    "Hello, World!",
    "12321",
    "racecar",
]

for text in tests:
    result = "палиндром" if is_palindrome(text) else "не палиндром"
    print(f"'{text}' – {result}")
