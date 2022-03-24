def divide_nums(n1, n2):
    return round((n1 / n2), 2)

n1 = int(input("Enter number one: "))
n2 = int(input("Enter number two: "))

print(f"The result is {divide_nums(n1, n2)}")