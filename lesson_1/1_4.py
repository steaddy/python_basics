n = input("Введите целое положительное число: ")
i = 0
the_max = 0
while i < len(n):
    current = int(n[i])
    if the_max < current:
        the_max = current
    i = i + 1

print(f"The biggest number is: {the_max}")