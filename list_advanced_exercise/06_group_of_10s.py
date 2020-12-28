import math

group_of_numbers = input().split(', ')
list_of_numbers = [int(el) for el in group_of_numbers]
boundary = 10
previous_boundary = 0
removed_elements = []


def roundup(x):
    return int(math.ceil(x / 10.0)) * 10


while roundup(max(list_of_numbers)) >= boundary:
    for el in list_of_numbers:
        if previous_boundary < el <= boundary:
            removed_elements.append(el)
    print(f"Group of {boundary}'s: {removed_elements}")
    removed_elements = []
    boundary += 10
    previous_boundary += 10
