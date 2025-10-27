import random

map = ["-", "-", "-", "-", "-"]
treasure = random.randint(0, 4)
Motivation=["YOU CAN DO IT CAPTAIN","YOU ARE VERY CLOSE LETSGO"]
found = False

while not found:
    guess = int(input("Guess the position (1–5): ")) - 1
    if guess == treasure:
        map[guess] = "💎"
        found = True
    else:
        map[guess] = "O"
        if guess < treasure:
            print("Too left! GO RIGHT 👉🏻")
        else:
            print("Too right! GO LEFT 👈🏻")
        print(random.choice(Motivation))
    print("Current Map:", map)

print("You found the treasure! 🪙")
