from re import match


# валдиция эмейла
def validate_email(email: str) -> bool:
    pattern = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"
    return bool(match(pattern, email))


# валдиция номера телефона
def validate_phone(phone: str) -> bool:
    pattern = r"^\+?7[\s-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}$"
    return bool(match(pattern, phone))


# валдиция УРЛА
def validate_url(url: str) -> bool:
    pattern = r"^https?://[\w.-]+\.[a-z]{2,}(/[\w./-]*)?$"
    return bool(match(pattern, url))


# массив множеств для теста работоспособности функций для валдиции
tests = [
    ("email", "ivan@example.com", validate_email),
    ("email", "invalid@", validate_email),
    ("phone", "+7 (999) 123-45-67", validate_phone),
    ("url", "https://example.com", validate_url),
    ("url", "not-a-url", validate_url),
]

for data_type, value, validator in tests:
    result = "OK" if validator(value) else "X"
    print(f"[{result}] {data_type}: {value}")
