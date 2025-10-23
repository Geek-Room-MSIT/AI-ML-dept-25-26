sentence = input("Enter a sentence with emojis: ")

mood_dict = {"love": 1, "😍": 1, "happy": 1, "like": 1,
             "hate": -1, "😫": -1, "sad": -1, "angry": -1}

positive = 0
negative = 0

for word, value in mood_dict.items():
    if word in sentence.lower():
        if value == 1:
            positive += 1
        elif value == -1:
            negative += 1

if positive > negative:
    print("Overall Mood: Positive 😊")
elif negative > positive:
    print("Overall Mood: Negative 😞")
else:
    print("Overall Mood: Neutral 😐")
