import random 

characters = ["a sleepy panda", "an alien", "a pirate", "a robot", "a clumsy ninja"]
places = ["to the jungle", "on Mars", "to a tech fest", "in the library", "in a haunted house", "inside a washing machine"]
verb1 = ["ate", "found", "got afraid of", "saw"]
objects = ["a laptop.", "a treasure map.", "a sandwich.", "a phone.", "an ice cream.", "a clock."] 
actions1 = ["started coding and", "started singing but", "started dancing but", "sneezed and", "built a rocket but", "lost WiFi and"]
actions2 = ["fell on the ground.", "fainted.", "lost memory.", "got panicked.", "got done of life."]

def make_story():
    char = random.choice(characters)
    p = random.choice(places)
    v1 = random.choice(verb1)
    obj = random.choice(objects)
    act1 = random.choice(actions1)
    act2 = random.choice(actions2)        
    story = f"Once {char} went {p} and {v1} {obj} It then {act1} {act2}"
    return(story)

n = int(input("How many stories do you want? "))

for i in range(n):
    print("\nStory:", i+1)
    print(make_story())
    
