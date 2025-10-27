import random

map = ["_", "_", "_", "_", "_"]
treasure = random.randint(0, 4)

found = False

while not found:
    guess = int(input("Guess the position (1-5): ")) - 1
    
    if guess == treasure:
        map[guess] = "💎"
        found = True
    else:
        if guess < treasure:
            print("Too left! ➡️")
        elif guess > treasure:
            print("Too right! ⬅️")
        
        if 0 <= guess < len(map):
            map[guess] = "O"
    
    print(" ".join(map))

print("You found the treasure! 🏆")
