import random 

map1 = ["_", "_", "_", "_", "_"] 
treasure = random.randint(0, 4) 
found = False 
print("Welcome to the Treasure Hunt Game!\n", map1, "\nThe treasure is hidden in one of these spots. Good luck finding it!")

while not found:
    guess = int(input("Guess the position (1-5): ")) - 1
    if guess == treasure:
        print("Amazing guess! You found the treasure!🏆")
        break
    else:
        if treasure-guess >= 2:
            print("Oops! Too left!")
        elif treasure-guess == 1:
            print("You got just a bit to the left!")
        elif guess-treasure >= 2:
            print("Oops! Too right!")
        elif guess-treasure == 1:
            print("You got just a bit to the right!")
        map1[guess] = 0
        print(map1)
