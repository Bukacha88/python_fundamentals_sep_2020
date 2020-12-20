data = input()
products = {}


while not data == 'buy':
    product, price, quantity = data.split()
    price = float(price)
    quantity = int(quantity)
    if product not in products:
        products[product] = [0, 0]
    products[product][0] = price
    products[product][1] += quantity

    data = input()
for key, value in products.items():
    print(f'{key} -> {(value[0] * value[1]):.2f}')
