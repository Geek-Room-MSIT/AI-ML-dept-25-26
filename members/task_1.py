sentence = input("Enter a sentence with emojis: ")

mood_dict = {
    "love": 1, "😍": 1, "happy": 1, "excited": 1, "joy": 1, "awesome": 1, "great": 1,
    "hate": -1, "😫": -1, "sad": -1, "angry": -1, "terrible": -1, "awful": -1, "bad": -1
}

positive = 0
negative = 0

for word, val in mood_dict.items():
    if word in sentence.lower():
        if val > 0:
            positive += 1
        else:
            negative += 1

if positive > negative:
    print("Overall Mood: Positive 😊")
elif negative > positive:
    print("Overall Mood: Negative 😢")
else:
    print("Overall Mood: Neutral 😐")
