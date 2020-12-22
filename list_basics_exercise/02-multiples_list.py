factor = int(input())
count = int(input())
number = 1
my_list = []

while len(my_list) < count:
    if number % factor == 0:
        my_list.append(number)
    number += 1
print(my_list)