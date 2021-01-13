import re
line = input()
pattern = r"(^>>)(?P<name>\w+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)($|\s)"
total_sum = 0
names = []
while not line == 'Purchase':
    match = re.match(pattern, line)
    if match:
        obj = match.groupdict()
        names.append(obj["name"])
        total_sum += float(obj["price"]) * int(obj["quantity"])

    line = input()
print('Bought furniture:')
for name in names:
    print(name)

print(f"Total money spend: {total_sum:.2f}")