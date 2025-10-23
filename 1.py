# 1.py
sentence = input("Enter a sentence with emojis: ")

mood_dict = {"love": 1, "😍": 1, "happy": 1, "hate": -1, "😫": -1, "sad": -1}

positive = 0
negative = 0

for key, value in mood_dict.items():
    count = sentence.count(key)
    if value > 0:
        positive += count
    else:
        negative += count  # Actually, since value is -1, I could do total += value * count, but separate counters feel clearer

if positive > negative:
    print("Overall Mood: Positive")
elif negative > positive:
    print("Overall Mood: Negative")
else:
    print("Overall Mood: Neutral")
