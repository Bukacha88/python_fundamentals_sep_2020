numbers = input().split()

numbers_to_remove = int(input())

numbers = list(map(int, numbers))
for i in range(numbers_to_remove):
    numbers.remove(min(numbers))
print(numbers)
