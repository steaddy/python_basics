def sum_from_string(string_with_numbers):
    return sum(list(map(int,(string_with_numbers.split()))))


res = 0

while True:
    res += sum_from_string(input("Введите числа через пробел: "))
    print(res)
    i = input("Закончить - q, продолжить - Enter: ")
    if i == 'q':
        break

