import random
characters = ["a sleepy panda", "an alien", "a pirate", "a robot", "a talking cat"]
places = ["in the jungle", "on Mars", "at a tech fest", "in the library", "at a pizza shop"]
objects = ["a laptop", "a treasure map", "a sandwich", "a phone", "a cup of coffee"]
actions = ["started coding", "fell asleep", "built a rocket", "lost their WiFi", "started dancing"]

how_many = int(input("How many stories do you want? "))
print("\nHere are your random stories:\n")

for i in range(how_many):
    char = random.choice(characters)
    place = random.choice(places)
    obj = random.choice(objects)
    action = random.choice(actions)
    
    print("Story " + str(i+1) + ": Once upon a time, " + char + " found " + obj + " " + place + " and " + action + "!")



