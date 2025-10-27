import random
objects = ["a laptop", "a treasure map", "a sandwich", "a phone"] 
actions = ["started coding", "fell asleep", "built a rocket", "lost their WiFi"]
characters = ["a sleepy panda", "an alien", "a pirate", "a robot"] 
places = ["in the jungle", "on Mars", "at a tech fest", "in the library"] 

def generate_story():
    n= int(input("how many stories do you want to generate? "))
    stories = []
    for x in range(n):
        obj = random.choice(objects)
        act = random.choice(actions)
        char = random.choice(characters)
        place = random.choice(places)
        story = f"Once upon a time, {char} found {obj} and {act} {place}."
        stories.append(story)
    for s in stories:
        print(s)

generate_story() 