import random
map = ["_", "_", "_", "_", "_"]
treasure = random.randint(0, 4)

guess=int(input("Enter number 1-5"))
if treasure==guess:
  print("You found the treasure")
else:
  if treasure>guess:
    print("Too left")
    map[guess]=0
    print(map)
  elif treasure<guess:
    print("Too right")
    map[guess]=0
    print(map)