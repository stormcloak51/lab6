ip = input("Введите IP-адрес: ")
# делим айпишник на октеты
parts = ip.split(".")

is_valid = len(parts) == 4

if is_valid:
    for part in parts:
        # октет - число, находится в диапозоне [0;255] и не начинается на 0, когда длина > 1
        if (
            not part.isdigit()
            or not (0 <= int(part) <= 255)
            or (len(part) > 1 and part[0] == "0")
        ):
            is_valid = False
            break

if is_valid:
    print(f"{ip} — корректный IP-адрес")
else:
    print(f"{ip} — некорректный IP-адрес")
