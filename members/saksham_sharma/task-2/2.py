import random

characters = ["a sleepy panda", "an alien","a pirate","a robot"]
places = ["in the jungle","at Mars","in the library","at the tech fest","at the road"]
objects = ["a laptop"," a tablet", "a PC","a mouse","a keyboard"]
actions = ["started coding","started singing", "started freelancing","started eating","started crying"]



how_many = int(input("How many stories do you want?:"))

for i in range(how_many):
    character=random.choice(characters)
    place=random.choice(places)
    object=random.choice(objects)
    action=random.choice(actions)

    print(f"Story{i+1}: Once upon a time {character} found {object} {place} and {action}")
    print("")
