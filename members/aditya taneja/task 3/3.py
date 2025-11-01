import random
pit = ["_", "_", "_", "_", "_"]
treasure = random.randint(0, 4)
found = False
print("Welcome to the Game of TREASUREEEE HUNT!")
print("There are 5 pits numbered 1 to 5. Try to find the pit where our treasure is hidden!\n")
while not found:
    guess = int(input("Guess the position (1-5): ")) - 1
    if guess < 0 or guess > 4:
        print("Please enter a number between 1 and 5!\n")
        continue
    if guess == treasure:
        pit[guess] = "💰✅"
        print("You found the treasure! 🎉")
        found = True
    else:
        pit[guess] = "❌"
        if guess < treasure:
            print("Too left! Try a bit to the right →")
        else:
            print("Too right! Try a bit to the left ←")
    print("Map:", pit)
    print()
print("Final Map:", pit)
print("Congrats! You completed the Treasure Hunt 🏴‍☠️")
