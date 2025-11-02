import random

characters = [
    "a sleepy panda", "an alien", "a pirate", "a robot", "a wizard", "a confused programmer",
    "a ninja cat", "a lost astronaut", "a talking banana", "a gamer ghost"
]

places = [
    "in the jungle", "on Mars", "at a tech fest", "in the library", "under the ocean",
    "on a spaceship", "at Hogwarts", "in a haunted house", "inside a computer", "on a flying island"
]

objects = [
    "a laptop", "a treasure map", "a sandwich", "a phone", "a magic wand", "a glowing stone",
    "a cup of coffee", "an old diary", "a mysterious USB drive", "a golden key"
]

actions = [
    "started coding", "fell asleep", "built a rocket", "lost their WiFi", "opened a portal",
    "invented a new dance move", "spoke to aliens", "won a dance battle", "discovered time travel",
    "forgot their password"
]

how_many = int(input("How many stories do you want? "))

for _ in range(how_many):
    story = (
        f"Once upon a time, {random.choice(characters)} found {random.choice(objects)} "
        f"{random.choice(places)} and {random.choice(actions)}!"
    )
    print(story)
