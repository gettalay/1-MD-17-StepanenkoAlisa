import csv

with open('данные.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)

    total_cost = 0
    shopping_list = []

    for row in reader:
        product, quantity, price = row
        cost = int(quantity) * int(price)
        total_cost += cost
        shopping_list.append(f"{product} - {quantity} шт. за {price} руб.")

print("Нужно купить:")
for item in shopping_list:
    print(item)
print(f"Итоговая сумма: {total_cost} руб.")
