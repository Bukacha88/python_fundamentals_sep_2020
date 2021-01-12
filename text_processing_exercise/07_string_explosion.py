sequence = list(input())

string = []
bomb = 0
for i in range(len(sequence)):
    if bomb > 0 and sequence[i] != '>':
        bomb -= 1
    elif sequence[i] == '>':
        string.append(sequence[i])
        bomb += int(sequence[i + 1])
    else:
        string.append(sequence[i])
print(''.join(string))