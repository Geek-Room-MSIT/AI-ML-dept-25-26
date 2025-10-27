#  Treasure Hunt Game 
import random
motivation=["don't be sad! Try again","you will guess it right now","you can do it Try again!","ohh ohh try again!!"]
map=["_","_","_","_","_",]
treasure = random.randint(0, 4) 
guess=int(input("guess where is the treasure from 1to 5 in a list"))-1
while guess!=treasure:
    randomMot=random.choice(motivation)
    if guess>treasure:
        print("Treasure not found (you are too right)")
    elif guess<treasure:
        print("Treasure not found (you are too left)")
    guess=int(input(f"{randomMot}"))-1
print("Hurray Treasure is found🎉 ") 
