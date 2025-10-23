import random 
# explain lists with characters, places, and actions
characters = ["A demon king" , "A wizard", "A dog", "An elf", "A pirate", "A assassin" , "A wise man"]
places = ["in the forest", "on the moon", "at the demon castle", "in a parallel world", "in a busy guild"]
actions = ["found a evil eye sword", "become a hero", "fought a dragon", "discovered a secret door to parallel world", "had a to deafeted by demon king"]

# Randomly pick one from each listed itmes
character = random.choice(characters)
place = random.choice(places)
action = random.choice(actions)

# Combine the selected items into a story
story = f"One day, {character} {place} and {action}.\nIt was the most unexpected event of their life!"

print(story)
