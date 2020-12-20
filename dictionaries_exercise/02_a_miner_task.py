resource = input()
goods = {}

while not resource == 'stop':
    quantity = int(input())
    if resource in goods:
        goods[resource] += quantity
    else:
        goods[resource] = quantity
    resource = input()

for key, value in goods.items():
    print(f"{key} -> {value}")