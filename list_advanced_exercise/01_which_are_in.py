list_one = input().split(', ')
list_two = input().split(', ')
list_three = []
for word in list_one:
    for el in list_two:
        if word in el:
            if word not in list_three:
                list_three.append(word)

print(list_three)
