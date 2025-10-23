import random
map = ["_", "_", "_", "_", "_"]
print("The treasure is hidden in one of the following places:    __  __  __  __  __  \n")
print("Make your guess to find the treasure!\n")

treasure = random.randint(0, 4)
found = False
while not found:
 guess = int(input("Guess the position (1-5): ")) - 1
 if guess==treasure:
     print("You found the treasure! 🏆")
     break
 else:
     discrepancy=abs(treasure-guess)
     print("You are", discrepancy, "places away from the treasure!")
