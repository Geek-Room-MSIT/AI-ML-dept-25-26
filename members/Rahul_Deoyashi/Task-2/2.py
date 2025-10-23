import random

characters = ["a sleepy panda", "an alien", "a pirate", "a robot", "a ninja", "a scientist"]
places = ["in the jungle", "on Mars", "at a tech fest", "in the library", "at the beach", "inside a volcano"]
objects = ["a laptop", "a treasure map", "a sandwich", "a phone", "a guitar", "a cup of coffee"]
actions = ["started coding", "fell asleep", "built a rocket", "lost their WiFi", "started dancing", "forgot their password"]

how_many = int(input("How many stories do you want? "))
count=1

for i in range(how_many):    
    random_character = random.choice(characters)
    random_place = random.choice(places)
    random_obj= random.choice(objects)
    random_action= random.choice(actions)    
    print(count,"--> Once upon a time,",random_character, "found", random_place, random_obj, "and", random_action)
    count+=1
    
