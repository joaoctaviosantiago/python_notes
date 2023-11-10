
player_position = (100, 200)
enemy_position = (500, 600)
print(f"Before: {player_position}, {enemy_position}")

player_position, enemy_position = enemy_position, player_position
print(f"After: {player_position}, {enemy_position}")
