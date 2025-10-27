#Task 2: Random Story Generator
import random
characters = ["a sleepy panda", "an alien", "a pirate", "a robot", "a ninja"]
places = ["in the jungle", "on Mars", "at a tech fest", "in the library", "in spaceship"]
objects = ["a laptop", "a treasure map", "a sandwich", "a phone", "a book"]
actions= ["started coding", "fell asleep", "built a rocket", "lost their WiFi", "started dancing"]
reason= ["to get full marks", "to get a placemnet", "to defeat monsters", "to sleep", "to destroy universe"]
num = int(input("How many stories do you want?\n"))
for i in range(num):
  print(f"\nStory {i+1}:")
  print(f"Once upon a time, {random.choice(characters)} found {random.choice(objects)} {random.choice(places)} and {random.choice(actions)} {random.choice(reason)}.\n")
