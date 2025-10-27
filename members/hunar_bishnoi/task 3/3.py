#Hide a treasure randomly in a list of 5 places. Player guesses until they find it.

import random

position = [1, 2, 3, 4, 5]
k = random.choice(position)

print("The treasure is hidden in one of these positions")
print("_ , _ , _ , _ , _")
print("")

t1 = int(input("GUESS THE PLACE: "))

while t1 != k:
    df = abs(k - t1) 
    if t1 < 1 or t1 > 5:
        print(" Choose a valid position between 1 and 5.")
    elif df == 3:
        print("COLD ")
    elif df == 2:
        print("WARM")
    elif df == 1:
        print("WARMER")

    t1 = int(input("TAKE ANOTHER GUESS: "))



print("YOU HAVE FOUND THE TREASURE!")
