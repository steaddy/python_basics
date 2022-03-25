def my_func(a, b, c):
    min_val = min(a, b, c)
    res = [a, b, c]
    res.remove(min_val)
    return sum(res)

print(my_func(8, 2, 10))