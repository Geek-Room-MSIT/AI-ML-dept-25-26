import random

game_map = ["_", "_", "_", "_", "_"]
treasure = random.randint(0, 4)
found = False

print("Welcome to the Treasure Hunt Game! 🏝️")

while not found:
    guess = int(input("Guess the position (1-5): ")) - 1

    if guess < 0 or guess > 4:
        print("Please enter a number between 1 and 5.")
        continue

    if guess == treasure:
        print("You found the treasure! 🏆")
        found = True
    elif guess < treasure:
        print("Too left! Try moving right →")
    else:
        print("Too right! Try moving left ←")

    game_map[guess] = "O"
    print("Map:", game_map)
