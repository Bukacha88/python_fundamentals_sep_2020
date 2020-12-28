hearts = input().split('@')
hearts = list(map(int, hearts))
data = input()

current_position = 0


def cupid_jump(nums, i):
    if i + current_position > len(hearts) - 1:
        nums[0] -= 2
        if nums[0] == 0:
            print(f"Place 0 has Valentine's day.")
        elif nums[0] < 0:
            print(f"Place 0 already had Valentine's day.")
    else:
        nums[i + current_position] -= 2
        if nums[i + current_position] == 0:
            print(f"Place {i + current_position} has Valentine's day.")
        elif nums[i + current_position] < 0:
            print(f"Place {i + current_position} already had Valentine's day.")

    return nums


while not data == 'Love!':
    command, index = data.split()
    index = int(index)
    cupid_jump(hearts, index)
    if current_position + index > len(hearts) - 1:
        current_position = 0
    else:
        current_position += index

    data = input()

print(f"Cupid's last position was {current_position}.")
hearts = [el for el in hearts if el > 0]
if len(hearts) > 0:
    print(f"Cupid has failed {len(hearts)} places.")
else:
    print("Mission was successful.")
