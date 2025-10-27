#treasure hunt game
import random

map = ["_", "_", "_", "_", "_"]
treasure = random.randint(0, 4)
found = False

while not found:
    print("Current Map:", " ".join(map))
    guess = int(input("Guess the position (1-5): ")) - 1

    if guess == treasure:
        print("You found the treasure! 🏆")
        found = True
    else:
        if guess < treasure:
            print("Too left!")
        elif guess > treasure:
            print("Too right!")
        map[guess] = "O"

print("Final Map:", " ".join(map))