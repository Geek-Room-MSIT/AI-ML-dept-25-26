from random import choice 
characters = ["a sleepy panda", "an alien", "a pirate", "a robot"]
places = ["in the jungle", "on Mars", "at a tech fest", "in the library"]
objects = ["a laptop", "a treasure map", "a sandwich", "a phone"]
actions = ["started coding", "fell asleep", "built a rocket", "lost their WiFi"]

c = choice(characters)
p = choice(places)
o = choice(objects)
a = choice(actions)
print(f"Once upon a time, {c} was {p} with {o} when they suddenly {a}.")