#Hide a treasure randomly in a list of 5 places. Player guesses until they find it.

import random 
def game():
    map = ["_", "_", "_", "_", "_"] 
    treasure = random.randint(0, 4) 
    found = False 
    while not found: 
        guess = int(input("Guess the position (1-5): ")) - 1
        if guess < treasure:
            print("Too Right")
            map[guess]=0
            print(map) 
        elif guess > treasure:
            print("Too left")
            map[guess]=0
            print(map) 
        else:
            print("You found the treasure! 🏆")
            found = True
            map[guess]="🏆"
            print(map)

game()