#Task 3: Treasure Humt Game
import random
map=["_","_","_","_","_"]
treasure=random.randint(0,4)
found = False
while not found:
  guess = int(input("Guess the position of the treasure(1-5):"))-1
  if(guess>4 or guess<0):
    print("Invalid input!")
  elif(treasure-guess>1):
    print("Hint:Too left!")
    map[guess]="O"
    print(f"Current Map:{map}")
  elif(treasure-guess==1):
    print("Hint:Go little right")
    map[guess]="O"
    print(f"Current Map:{map}")
  elif(treasure-guess<-1):
    print("Hint:Too right!")
    map[guess]="O"
    print(f"Current Map:{map}")
  elif(treasure-guess==-1):
    print("Hint:go little left!")
    map[guess]="O"
    print(f"Current Map:{map}")
  else:
    print("You found the treasure!🏆")
    map[guess]="X"
    print(f"Current Map:{map}")
    found = True
