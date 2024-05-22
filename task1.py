import json

with open('products.json') as json_file:
    data = json.load(json_file)

products = data['products']

for product in products:
    name = product['name']
    price = product['price']
    weight = product['weight']
    available = "В наличии" if product['available'] else "Нет в наличии"

    print(f"Название: {name}")
    print(f"Цена: {price}")
    print(f"Вес: {weight}")
    print(available)
    print()
