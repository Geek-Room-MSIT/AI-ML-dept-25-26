import random

characters = ["a sleepy panda", "an alien", "a pirate", "a robot"]
places = ["in the jungle", "on Mars", "at a tech fest", "in the library"]
objects = ["a laptop", "a treasure map", "a sandwich", "a phone"]
actions = ["started coding", "fell asleep", "built a rocket", "lost their WiFi"]

characters_1 = random.choice(characters)
places_1 = random.choice(places)
objects_1 = random.choice(objects)
actions_1 = random.choice(actions)

print(f"Once upon a time, {characters_1} found {objects_1} in  {places_1} while they {actions_1}")
