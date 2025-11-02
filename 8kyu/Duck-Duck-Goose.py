# The objective of Duck, duck, goose is to walk in a circle, tapping on each player's head until one is chosen.

# Task:

# Given an array of Player objects and a position (first position is 1), return the name of the chosen Player.
# name is a property of Player objects, e.g Player.name

# we want to pick a player by counting “goose” steps around the circle and wrap back to the start when we pass the end.
arr = [name for name in "abcdcefghz"]
print(arr)


def duck_duck_goose(players, goose):
    num_players = len(players)
    chosen_index = (goose - 1) % num_players # this implements counting in a circle.

    return players[chosen_index].name

duck_duck_goose(arr, 11)


