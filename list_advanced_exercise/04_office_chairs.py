rooms = int(input())
free_chairs = 0
game_on = 0
for room in range(1, rooms + 1):
    chairs = input().split(' ')
    if len(chairs[0]) >= int(chairs[1]):
        free_chairs += len(chairs[0]) - int(chairs[1])
        game_on += 1
    elif len(chairs[0]) < int(chairs[1]):
        needed_chairs_in_room = int(chairs[1]) - len(chairs[0])
        print(f"{needed_chairs_in_room} more chairs needed in room {room}")
if game_on == rooms:
    print(f"Game On, {free_chairs} free chairs left")
