electrons = int(input())

index = 1

electrons_shell = []
while electrons > 0:

    number_of_electrons = 2 * index ** 2
    if number_of_electrons > electrons:
        electrons_shell.append(electrons)
        break
    electrons_shell.append(number_of_electrons)
    electrons -= int(number_of_electrons)
    index += 1
print(electrons_shell)