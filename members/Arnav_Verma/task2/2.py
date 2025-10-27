import random

characters = ["a sleepy panda", "a time-traveling alien", "a clumsy pirate", "an overworked robot"]
places = ["in a jungle full of WiFi", "on Mars during rush hour", "at a chaotic tech fest", "inside a silent library"]
objects = ["a magical laptop", "a broken sandwich", "a glowing treasure map", "a confused phone"]
actions = ["started coding in their dreams", "fell asleep mid-battle", "built a rocket from trash", "lost their last byte of memory"]
twists = ["Then they realized it was all a dream.", "Suddenly, everything turned into cheese!", "A monkey applauded loudly.", "And they became famous overnight!"]

how_many = int(input("How many stories do you want to hear? "))

for i in range(1, how_many + 1):
    char = random.choice(characters)
    place = random.choice(places)
    obj = random.choice(objects)
    act = random.choice(actions)
    twist = random.choice(twists)

    print(f"\n📖 Story {i}:")
    print(f"Once upon a glitch, {char} found {obj} {place}.")
    print(f"They {act} 🤖 {twist}")
