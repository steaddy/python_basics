my_list = [7, 5, 3, 3, 2]

n = 0
while n < 5:
    add_to_list = int(input("Введите число от 1 до 9: "))
    i = 0
    length = len(my_list)
    while i < length:
        print(i)
        if my_list[i] <= add_to_list:
            my_list.insert(i, add_to_list)
            break
        elif my_list[-1] > add_to_list:
            my_list.append(add_to_list)
            break
        i += 1
    print(my_list)
    n += 1
