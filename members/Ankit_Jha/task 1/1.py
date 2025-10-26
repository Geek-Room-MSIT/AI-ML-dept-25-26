s = input("Enter your sentence with emojis: ").lower()

mood_dict = {
    "love": 2, "😍": 2, "amazing": 2, "great": 1, "happy": 1,
    "hate": -2, "😫": -2, "angry": -2, "sad": -1, "terrible": -2
}

postive_mood = 0
negetive_mood = 0

for mood, value in mood_dict.items():
    if mood in s:
        if value > 0:
            postive_mood += value
        else:
            negetive_mood += abs(value)

print("\n Analyzing your mood ...")

if postive_mood > negetive_mood:
    print("Overall Mood: Positive and Cheerful")
elif negetive_mood > postive_mood:
    print("Overall Mood: Negative or Upset")
else:
    print("Overall Mood: Neutral or Mixed Feelings.")