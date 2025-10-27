import random

map = ["_", "_", "_", "_", "_"]
treasure = random.randint(0, 4)

found = False

print("Welcome to Treasure Hunt! 🏴‍☠️")
print("Guess the position where the treasure is hidden (1-5)")
print("Current map:", " ".join(map))

while not found:
    guess = int(input("\nGuess the position (1-5): ")) - 1
    
    # Validate input
    if guess < 0 or guess > 4:
        print("Invalid position! Please choose between 1 and 5.")
        continue
    
    # Check if guess matches treasure position
    if guess == treasure:
        map[guess] = "X"  
        print("Current map:", " ".join(map))
        found = True
    else:
        # Mark tried spot
        map[guess] = "O"
        
        # Give hints
        if guess < treasure:
            print("Too left! Try moving right.")
        else:
            print("Too right! Try moving left.")
        
        # Show updated map
        print("Current map:", " ".join(map))

print("\n🎉 You found the treasure! 🏆")

