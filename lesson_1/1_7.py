start = int(input("Введите начальную дистанцию: "))
result = int(input("Введите желаемую дистанцию: "))
days = 0

while result > start:
    days = days + 1
    start = start * 1.1

print(f"Для достижения результата потребуется {days} дней")
