def vigenere_cipher(text: str, key: str, decrypt: bool = False) -> str:
    result = []
    key = key.lower()
    key_index = 0

    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            # если длина ключа больше чем сам текст,
            # мы с помощью остатка от деления на длину ключа будем снова
            # повторять ключ
            shift = ord(key[key_index % len(key)]) - ord("a")
            if decrypt:
                shift = -shift
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
            key_index += 1
        else:
            result.append(char)

    return "".join(result)


text = input("Введите текст: ")
key = input("Введите ключ: ")

encrypted = vigenere_cipher(text, key)
decrypted = vigenere_cipher(encrypted, key, decrypt=True)

print(f"Зашифровано: {encrypted}")
print(f"Расшифровано: {decrypted}")
