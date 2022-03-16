input_list = input("Введите данные через пробел: ").split()
i = 0
list_length = len(input_list)
if list_length % 2 != 0:
    list_length -= 1
while i < list_length:
    if i % 2 != 0:
        temp = input_list[i - 1]
        input_list[i - 1] = input_list[i]
        input_list[i] = temp
    i += 1


print(input_list)

