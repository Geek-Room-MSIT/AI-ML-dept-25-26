# Emoji mood generator
sentence = input("enter a sentence with emojis: ")

mood_dict = {
    "love": 1, "😍": 1, "happy": 1,
    "hate": -1, "😫": -1, "sad": -1
}

positive = 0# for 1
negative = 0# for -1

for key, value in mood_dict.items():
    if key in sentence:
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