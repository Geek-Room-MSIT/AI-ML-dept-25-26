#Task 2: Random Story Generator

import random

characters = ["a sleepy panda", "an alien", "a pirate", "a robot"]
places = ["in the jungle", "on Mars", "at a tech fest", "in the library"]
objects = ["a laptop", "a treasure map", "a sandwich", "a phone"]
actions = ["started coding", "fell asleep", "built a rocket", "lost their WiFi"]

#Ask the user how many stories to generate
how_many = int(input("How many stories do you want? "))

# TODO: use random.choice() to pick one from each list
for i in range(how_many):

    character = random.choice(characters)
    place = random.choice(places)
    obj = random.choice(objects)
    action = random.choice(actions)

#story
    print(f"\nstory {i+1}:")
    print(f"once upon a time, {character} found {obj} {place} and {action}!")

print("--End of stories--")
