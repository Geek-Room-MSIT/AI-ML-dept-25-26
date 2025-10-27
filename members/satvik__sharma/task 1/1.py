sentence = input("Enter a sentence with emojis: ")

mood_dict = {"love": 1, "🥰": 1, "happy": 1, "hate": -1, "😔": -1, "sad": -1}

positive=negative=0

for key in mood_dict:
    if key in sentence:
        if mood_dict[key] == 1:
            positive += 1
        elif mood_dict[key] == -1:
            negative += 1

if positive > negative:
    print("Overall Mood: Positive 😊")
elif negative > positive:
    print("Overall Mood: Negative ☹️")
else:
    print("Overall Mood: Neutral 😐")
