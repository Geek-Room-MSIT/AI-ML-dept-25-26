sentence = input("Enter the sentence: ")
mood_dict = {"love": 1, "😍": 1, "happy": 1, "hate": -1, "😫": -1, "sad": -1}

positive = 0
negative = 0

for key in mood_dict.keys():
    if key in sentence:
        if mood_dict[key]== 1:
            positive += 1

        else:
            negative += 1

if positive > negative:
    print("Overall Mood is Positive")
elif positive < negative:
    print("Overall Mood is Negative")
else:
    print("Mood is Neutral")
