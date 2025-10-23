import random #for importing random support or location for treasure hunt

# List of 5 places
places = ["Forest", "Cave", "Beach", "Mountain", "Desert" , "Demon castle" , "Hidden labyrinth" , "dark abyss"]

# Pick a random place for the treasure
treasure = random.choice(places)

# Tell the player how to play
print("Welcome to the Lost Hunt Game!")
print("Guess where the treasure is hidden from these places:")
print(places)

# Keep asking until the guess is correct
guess = ""  # We start with an empty guess
while guess != treasure:
    guess = input("Enter your opinion: ")

# Check if the guess is correct
    if guess == treasure:
        print(f"Congrats!You’ve finally uncovered the treasure hidden deep within the {treasure}!")
    else:
        print("Pathetic. Enjoy your defeat. Thanks for playing, loser.")

# End of the game
print("Thanks for playing… though you’ll only remember this moment as your biggest mistake.")
