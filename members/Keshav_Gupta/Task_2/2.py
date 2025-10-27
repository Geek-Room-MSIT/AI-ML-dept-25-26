import random

characters = ["a sleepy panda", "an alien", "a pirate", "a robot"]
places = ["in the jungle", "on Mars", "at a tech fest", "in the library"]
objects = ["a laptop", "a treasure map", "a sandwich", "a phone"]
actions = ["started coding", "fell asleep", "built a rocket", "lost their WiFi"]

how_many = int(input("How many stories do you want? "))

for i in range(how_many):
    char = random.choice(characters)
    place = random.choice(places)
    obj = random.choice(objects)
    action = random.choice(actions)
    
    print(f"\nStory {i+1}:")
    print(f"Once upon a time, {char} was {place}.")
    print(f"They found {obj} and {action}!")