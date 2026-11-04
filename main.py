from re import match

json_str = input("Введите JSON-строку: ").strip()

# паттерн json'а
json_pattern = r'^\{\s*("[^"]+"\s*:\s*("[^"]*"|\d+|true|false|null)\s*(,\s*"[^"]+"\s*:\s*("[^"]*"|\d+|true|false|null)\s*)*)?\}$'

if match(json_pattern, json_str):
    print("Корректная JSON-строка")
else:
    print("Некорректная JSON-строка")
