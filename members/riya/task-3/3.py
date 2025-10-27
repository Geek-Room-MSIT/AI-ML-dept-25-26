#TASK 3: Treasure Hunt Game

import random

map = ["_", "_", "_", "_", "_"]

#treasure position

treasure = random.randint(1,5)
found = False

print("Welcome to treasure hunt!")
print("Map positions: 1 2 3 4 5")
print(map)

while not found:
    guess = int(input("Guess the position (1-5): "))

    if guess < 1 or guess > 5:
        print("Please guess a number between 1 and 5!")
        continue
    
    if guess == treasure:
        map[guess-1] = "X"
        print("You found the treasure!")
        print(map)
        found = True
    else:
        map[guess-1] = "0"
        if guess < treasure:
            print("Too left! Try a higher number.")
        else:
            print("Too right! Try a lower number.")
        print(map)
