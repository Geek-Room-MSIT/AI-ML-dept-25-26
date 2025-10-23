import random

map = ["_","_","_","_","_"]

treasure = random.randint(0,4)

found = False
 
while not found:
    
    guess = int(input("Guess the position (0-4) where treasure is: "))
    if guess == treasure:
        found = True

    elif guess<treasure:
        map[guess]=0
        print("Too left")
        print("Map::", map)
        
    else:
        map[guess]=0
        print("Too right")
        print("Map::", map)
        
    
print("You found the treasure!")