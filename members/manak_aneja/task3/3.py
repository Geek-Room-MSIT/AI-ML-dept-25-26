import random
map = ["_", "_", "_", "_", "_"]

def game():
    print("welcome to the treasure hunt!")
    print(" ".join(map))
    treasure_position = random.randint(0, 4)
    while True:
        guess = int(input("guess the position (1-5): ")) -1 
        if guess < 0 or guess > 4:
            print("please choose a position between 1 and 5.")
            continue
        if guess == treasure_position:
            print("congratulations! you found the treasure!🏆")
            map[guess] = "X"
            print(" ".join(map))
            break
        else:
            map[guess] = "O"
            print("no treasure here, try again 😔☝️")
            if guess < treasure_position:
                print("too left!")
            elif guess > treasure_position:
                print("too right!") 
            print("current map: ")
            print(" ".join(map))
game()