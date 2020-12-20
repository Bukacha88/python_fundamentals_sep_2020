import sys

n = int(input())
sum_even = 0.0
sum_odd = 0.0
min_number_odd = sys.maxsize
max_number_odd = -sys.maxsize
min_number_even = sys.maxsize
max_number_even = -sys.maxsize

for i in range(1, n + 1):
    number = float(input())
    if i % 2 == 0:
        sum_even += number
        if number > max_number_even:
            max_number_even = number
        if number < min_number_even:
            min_number_even = number

    else:
        sum_odd += number
        if number > max_number_odd:
            max_number_odd = number
        if number < min_number_odd:
            min_number_odd = number
print(f"OddSum={sum_odd:.2f},")
if min_number_odd != sys.maxsize:
    print(f"OddMin={min_number_odd:.2f},")
else:
    print(f"OddMin=No,")
if max_number_odd != -sys.maxsize:
    print(f"OddMax={max_number_odd:.2f},")
else:
    print(f"OddMax=No,")
print(f"EvenSum={sum_even:.2f},")
if min_number_even != sys.maxsize:
    print(f"EvenMin={min_number_even:.2f},")
else:
    print(f"EvenMin=No,")
if max_number_even != -sys.maxsize:
    print(f"EvenMax={max_number_even:.2f}")
else:
    print(f"EvenMax=No")


