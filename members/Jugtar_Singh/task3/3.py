from random import randint

map = ["_", "_", "_", "_", "_"]
treasure = randint(0, 4)
found = False
while not found:
    guess = int(input("Pick another number between 1 and 5: "))
    if guess - 1 == treasure:
        found = True
        print("You found the treasure!")
    else:
        if guess - 1 < treasure:
            print("The treasure is to the right.")
        else:
            print("The treasure is to the left.")
