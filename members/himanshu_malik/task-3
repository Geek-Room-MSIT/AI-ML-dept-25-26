import random

map = ["_", "_", "_", "_", "_"] 
treasure = random.randint(0, 4)

found = False
while found == False:
    guess = int(input("What's your guess? (Choose from 1-5)\n"))
    if guess not in (1,2,3,4,5):
        print("Incorrect input")
        continue
    if guess-1 == treasure:
        print("Congrations, you've proven yourself to be a fine pirate, matey!")
        found = True
    elif guess-1 > treasure:
        print("Close! Try a little to left")
    else:
        print("Need a hint? Pick something from the right side.")
