string_of_numbers = input()
my_list = string_of_numbers.split(" ")
list_of_opposite_numbers = []
new_number = 0
for i in range(len(my_list)):
    new_number += int(my_list[i])
    list_of_opposite_numbers.append(-new_number)
    new_number = 0
print(list_of_opposite_numbers)
