earnings = int(input("Введите сумму выручки: "))
expenses = int(input("Введите сумму издержек: "))
result = earnings - expenses
if result >= 0:
    print(f"Ваша прибыль составила: {result}")
    print(f"Рентабельность составила: {int(result / earnings * 100)} процентов")
    employees_number = int(input("Введите количество работников: "))
    print(f"Прибыль на одного сотрудника составила: {int(result / employees_number)}")
else:
    print(f"Ваши убытки составили: {result}")
