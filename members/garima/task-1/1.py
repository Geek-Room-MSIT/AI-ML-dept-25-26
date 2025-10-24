
print("How was your day")
sentence = input("Enter a sentence with emojis or words: ")

mood_dict = {
    "love": 1, "happy": 1, "great": 1, "😊": 1, "😍": 1,"hate": -1, "sad": -1, "angry": -1, 
    "😢": -1, "😡": -1
}

positive = 0
negative = 0

for word, value in mood_dict.items():
    if word in sentence:
        if value > 0:
            positive += 1
        else:
            negative += 1

if positive > negative:
    print("Overall Mood: Positive 😀\n Have a nice day")
elif negative > positive:
    print("Overall Mood: Negative 😞\n Sending good vibes")
else:
    print("Overall Mood: Neutral 😐\n")
