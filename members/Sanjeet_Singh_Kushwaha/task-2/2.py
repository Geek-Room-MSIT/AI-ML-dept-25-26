import random

numbers = int(input("How many number of stories do u want? -->"))

for i in range(2):
    
    characters = ["Newton", "an alien", "Joker", "Whale"]

    places = ["in the circus", "in area 51", "in the sea", "under the apple tree"]

    actions = ["juggling", "walking", "swimming", "reading book"]

    character = random.choice(characters)
    place = random.choice(places)
    action = random.choice(actions)
    
    print(f"Story {i+1}:\nOnce upon a time, {character} was {action} in the {place}. \
But soon, {character} decided to leave and start {random.choice(actions)} {random.choice(places)}.\n"
) 
    
    