import random

map=["_","_","_","_","_"]

treasure = random.randint(0, 4)

found = False

print("Welcome to the Treasure Hunt Game! 🏴‍☠️")
print("Try to find the treasure hidden in one of these 5 spots:")
print(" ".join(map))

while not found:
    guess = int(input("Guess the position (1-5): ")) - 1

    if guess < 0 or guess > 4:
        print("Please enter a number between 1 and 5!")
        continue

    if guess == treasure:
        map[guess] = "🏆"
        print(" ".join(map))
        print("You found the treasure! 🏆🎉")
        found = True
        
    else:
        map[guess] = "O"  # Mark tried spots
        print(" ".join(map))
        if guess < treasure:
            print("Too left! ➡️")
        else:
            print("Too right! ⬅️")
