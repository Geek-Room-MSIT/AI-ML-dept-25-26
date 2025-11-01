
import random

characters = ["a sleepy cat", "an ant", "a lady", "a robot", "a coder"]
places = ["in the jungle", "on Mars", "at a hackathon", "in a library", "under the sea"]
objects = ["a laptop", "a treasure map", "a sandwich", "a phone", "a magic key"]
actions = ["started coding", "fell asleep", "built a rocket", "lost Wi-Fi", "learned dance"]

count = int(input("How many stories do you want? "))

for i in range(count):
    c = random.choice(characters)
    p = random.choice(places)
    o = random.choice(objects)
    a = random.choice(actions)

    print(f"\nStory {i+1}:")
    print(f"Once upon a time, {c} {a} {p}.")
    print(f"They found {o} and you are still single!")
