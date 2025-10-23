# 3.py - Treasure Hunt Game
import random

game_map = ["_", "_", "_", "_", "_"]
treasure = random.randint(0, 4)
found = False

while not found:
    print("Current Map:", " ".join(game_map))
    guess = int(input("Guess the position (1-5): ")) - 1

    if guess == treasure:
        game_map[guess] = "🏆"
        print("You found the treasure! 🏆")
        found = True
    else:
        game_map[guess] = "O"
        if guess < treasure:
            print("Too left! Try a higher number →")
        else:
            print("Too right! Try a lower number ←")

    print()

print("Final Map:", " ".join(game_map))
