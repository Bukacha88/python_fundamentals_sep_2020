key_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
legendary_items = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}
junk = {}
line = input()
enough = False
key_mat = ''
while True:
    data = line.casefold().split()
    for i in range(1, len(data), 2):
        if data[i] in key_materials:
            key_materials[data[i]] += int(data[i-1])
            if key_materials[data[i]] >= 250:
                key_materials[data[i]] -= 250
                key_mat = legendary_items[data[i]]
                enough = True
                break
        elif data[i] in junk:
            junk[data[i]] += int(data[i-1])
        else:
            junk[data[i]] = int(data[i-1])
    if enough:
        print(f"{key_mat} obtained!")
        break
    line = input()
junk = sorted(junk.items(), key=lambda x: x[0])
key_materials = sorted(key_materials.items(), key=lambda x: (-x[1], x[0]))
for key, value in key_materials:
    print(f'{key}: {value}')
for key, value in junk:
    print(f'{key}: {value}')