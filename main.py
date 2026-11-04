def caesar_cipher(text: str, shift: int) -> str:
    """шифрует текст шифром цезаря"""
    result = []
    for char in text:
        # проверяем входит ли символ в алфавит
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            # делаем сдвиг буквы на shift позиций
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)
    return "".join(result)


original = "Hello, World!"
encrypted = caesar_cipher(original, 3)
print(f"Оригинал: {original}")
print(f"Зашифровано: {encrypted}")

decrypted = caesar_cipher(encrypted, -3)
print(f"Расшифровано: {decrypted}")
