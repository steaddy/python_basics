def my_func(a, b):
    return a ** b


def my_func_2(a, b):
    res = a
    for i in range(b - 1):
        res = res * a
    return res

print(my_func(0.25,-8))
print(my_func_2(0.25,-8))

# Только если степень целое положительное число