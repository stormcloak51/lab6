students = [
    ("Иван", 25, 4.5),
    ("Мария", 22, 4.85),
    ("Пётр", 30, 4.2),
    ("Анна", 20, 4.95),
]

# header
print(f"{'Имя':<10} {'Возраст':>8} {'Балл':>8}")
print("-" * 28)

# data
for name, age, gpa in students:
    print(f"{name:<10} {age:>8} {gpa:>8.2f}")

print("-" * 28)
avg_gpa = sum(s[2] for s in students) / len(students)
print(f"{'Средний балл':<8} {'':>6} {avg_gpa:>8.2f}")
