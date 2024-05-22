import json


#добавлениe нового продукта в файл
def add_product():
    name = input("Введите название продукта: ")
    price = float(input("Введите цену продукта: "))
    weight = float(input("Введите вес продукта: "))
    available = input("Есть ли продукт в наличии? (да/нет): ").lower() == 'да'

    with open('products.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    new_product = {
        "name": name,
        "price": price,
        "weight": weight,
        "available": available
    }
    data['products'].append(new_product)

    with open('products.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

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

add_product()

with open('products.json') as json_file:
    updated_data = json.load(json_file)

print("\nОбновленные данные:")
for product in updated_data['products']:
    name = product['name']
    price = product['price']
    weight = product['weight']
    available = "В наличии" if product['available'] else "Нет в наличии"

    print(f"Название: {name}")
    print(f"Цена: {price}")
    print(f"Вес: {weight}")
    print(available)
    print()
