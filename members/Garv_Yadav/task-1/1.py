# 1.py - Emoji Mood Analyzer
sentence = input("Enter a sentence with emojis: ").lower()

mood_dict = {"love": 1, "😍": 1, "happy": 1,
             "hate": -1, "😫": -1, "sad": -1}

positive = 0
negative = 0

for word, value in mood_dict.items():
    if word in sentence:
        if value > 0:
            positive += 1
        else:
            negative += 1

if positive > negative:
    print("Overall Mood: Positive 😊")
elif negative > positive:
    print("Overall Mood: Negative 😞")
else:
    print("Overall Mood: Neutral 😐")
