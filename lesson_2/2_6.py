goods = []

#goods = [(1, {'название': 'Картошка', 'цена': '20', 'количество': '50', 'ед': 'кг'}), (2, {'название': 'Соль', 'цена': '30', 'количество': '48', 'ед': 'упак'}), (3, {'название': 'Ручка', 'цена': '23', 'количество': '44', 'ед': 'шт'})]

items = 0
characteristics = 0

while items < 3:
    number = int(input("Введите номер товара: "))
    goods.append((number, {}))
    name = input("Введите название товара: ")
    goods[items][1]['название'] = name
    price = input("Введите цену товара: ")
    goods[items][1]['цена'] = price
    quantity = input("Введите количество товара: ")
    goods[items][1]['количество'] = quantity
    unit_of_measurement = input("Введите единицу измерения товара: ")
    goods[items][1]['ед'] = unit_of_measurement
    items += 1


analytics = {}

for item in goods:
    for characteristic in item[1]:
        if characteristic not in analytics:
            analytics[characteristic] = []
        analytics[characteristic].append(item[1][characteristic])

print(analytics)

