#Emoji Mood Analyzer

sentence = input("Enter a sentence with emojis: ")

mood_dict = {"love": 1, "😍": 1, "happy": 1, "hate": -1, "😫": -1, "sad": -1}

#TODO: initialize positive = 0, negative = 0

positive = 0
negative = 0

# TODO: loop through mood_dict keys and count how many are in sentence

for word, value in mood_dict.items():
    if word in sentence:
        if value == 1:
            positive += 1
        elif value == -1:
            negative += 1

print("Positive words count:", positive)
print("Negative words count:", negative)

# TODO: compare and print result like "Overall Mood: Positive/Negative/Neutral"

if positive > negative:
    print("Overall Mood: Positive")
elif negative > positive:
    print("Overall Mood: Negative")
else:
    print("Overall Mood: Neutral")
