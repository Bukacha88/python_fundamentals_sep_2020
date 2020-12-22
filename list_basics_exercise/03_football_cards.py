cards = input()
list_of_cards = list(cards.split(" "))
list_of_cards = list(dict.fromkeys(list_of_cards))
is_terminated = False
team_a = 11
team_b = 11
for char in list_of_cards:
    if 'A' in char:
        team_a -= 1
    elif 'B' in char:
        team_b -= 1
    if team_a < 7 or team_b < 7:
        is_terminated = True
        break
print(f"Team A - {team_a}; Team B - {team_b}")
if is_terminated:
    print("Game was terminated")







