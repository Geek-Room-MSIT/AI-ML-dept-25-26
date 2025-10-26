import random
import time

treasure_map = ["_", "_", "_", "_", "_"]
treasure_spot = random.randint(0, 4)
attempts = 0
found = False

print("Welcome to the Treasure Hunt!")
print("Find the hidden trophy somewhere in the 5 spots!")
print("Map:", treasure_map)

while not found:
    try:
        guess = int(input("\nChoose a spot (1–5): ")) - 1
        attempts += 1

        if guess < 0 or guess > 4:
            print("Enter a number between 1 and 5.")
            continue

        print("Scanning your choice...")
        time.sleep(0.8)

        if guess == treasure_spot:
            treasure_map[guess] = "🏆"
            print("\nYou found the treasure in", attempts, "tries!")
            print("Final Map:", treasure_map)
            found = True
        else:
            treasure_map[guess] = "❌"
            if guess < treasure_spot:
                print("Hint: The treasure is to the RIGHT!")
            else:
                print("Hint: The treasure is to the LEFT!")
            print("Map now looks like:", treasure_map)

    except ValueError:
        print("Please enter a valid number!")