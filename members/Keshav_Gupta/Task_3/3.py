import random

map = ["_", "_", "_", "_", "_"]
treasure = random.randint(0, 4)

found = False

while not found:
    guess = int(input("Guess the position (1-5): ")) - 1
    map[guess] = "O"
    
    diff = treasure - guess
    hints = ["You found the treasure! 🏆", "Too right!", "Too left!"]
    result = (diff > 0) * 2 + (diff < 0)
    
    print(hints[result])
    print()
    found = (diff == 0)