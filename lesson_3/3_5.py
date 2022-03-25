def sum_from_string(string_with_numbers):
    return sum(list(map(int,(string_with_numbers.split()))))


res = 0

while True:
    quit_cycle = False
    temp_str = input("Введите числа через пробел (для выхода введите 'q'): ")
    if 'q' in temp_str:
        quit_cycle = True
        temp_str = temp_str.replace('q', '')

    res += sum_from_string(temp_str)
    print(res)
    if quit_cycle:
        break


