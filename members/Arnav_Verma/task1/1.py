s = input("💭 Enter your sentence with emojis: ").lower()

mood_dict = {
    "love": 2, "😍": 2, "amazing": 2, "great": 1, "happy": 1,
    "hate": -2, "😫": -2, "angry": -2, "sad": -1, "terrible": -2
}

pos_mood = 0
neg_mood = 0

for mood, value in mood_dict.items():
    if mood in s:
        if value > 0:
            pos_mood += value
        else:
            neg_mood += abs(value)

print("\n Analyzing your mood ...")

if pos_mood > neg_mood:
    print("Overall Mood: Positive and Cheerful")
elif neg_mood > pos_mood:
    print("Overall Mood: Negative or Upset")
else:
    print("Overall Mood: Neutral or Mixed Feelings.")
