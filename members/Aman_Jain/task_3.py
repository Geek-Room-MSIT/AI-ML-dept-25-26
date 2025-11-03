import random

positions = {1: "_", 2: "_", 3: "_", 4: "_", 5: "_"}
treasure = random.randint(1, 5)
found = False

print("Welcome to the Treasure Hunt! Guess the treasure position (1–5).")

while not found:
    guess = int(input("Enter your guess (1–5): "))
    if guess == treasure:
        positions[guess] = "🏆"
        print(" ".join(positions.values()))
        print("You found the treasure!")
        found = True
    elif 1 <= guess <= 5:
        positions[guess] = "O"
        print("Too left!" if guess > treasure else "Too right!")
        print(" ".join(positions.values()))
    else:
        print("Please guess a number between 1 and 5.")
