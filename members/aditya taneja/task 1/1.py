sentence = input("Enter a sentence with emojis: ")
mood_dict = {
    "😘": 1,
    "😍": 1,
    "happy": 1,
    "great": 1,
    "hate": -1,
    "😫": -1,
    "sad": -1,
    "angry": -1,
    "😭": -1
}

positive = 0
negative = 0

for emoji in mood_dict:
    if emoji in sentence.lower():
        if mood_dict[emoji] == 1:
            positive += 1
        elif mood_dict[emoji] == -1:
            negative += 1

if positive > negative:
    print("Overall Mood: Positive++")
elif negative > positive:
    print("Overall Mood: Negative--")
else:
    print("Overall Mood: Neutral")
