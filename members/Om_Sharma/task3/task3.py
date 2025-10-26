import random

map = ["_", "_", "_", "_", "_"]
treasure = random.randint(0, 4)

found = False

print("Welcome to Treasure Hunt!")
print("Find the treasure hidden in positions 1-5!")
print("Initial map:", " ".join(map))

while not found:
    guess = int(input("Guess the position (1-5): ")) - 1
    
    if guess < 0 or guess > 4:
        print("Please enter a number between 1 and 5!")
        continue
    
    if guess == treasure:
        found = True
        map[guess] = ":)"  
        print(" ".join(map))
        print("You found the treasure! :) ")
    else:
        if guess < treasure:
            print("Try going RIGHT.")
        else:
            print("Try going LEFT.")
        
        map[guess] = "0"
        
        print("Current map:", " ".join(map))
        print()
