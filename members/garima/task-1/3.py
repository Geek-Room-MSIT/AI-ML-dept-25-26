import random

print("Welcome to Treasure Hunt!")
print("Guess the treasure position (1 to 5):")

map_list = ["-"] * 5
treasure = random.randint(0, 4)
found = False

while not found:
    guess = int(input("Enter your guess (1 to 5): ")) - 1

    if guess < 0 or guess > 4:
        print("Please enter a number between 1 and 5 only!")
        continue 
    if guess == treasure:
        map_list[guess] = "🏆"
        print("You found the treasure! 🏆")
        print(" ".join(map_list))
        found = True
    else:
        map_list[guess] = "X"
        if guess > treasure:
            print("Too left!")
        else:
            print("Too right!")
        print(" ".join(map_list))

