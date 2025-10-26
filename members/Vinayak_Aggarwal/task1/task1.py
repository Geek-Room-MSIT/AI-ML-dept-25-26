def analyze_mood(sentence):
    count = 0
    mood_dict = {"love": 1, "😍": 1, "happy": 1, "hate": -1, "😫": -1, "sad": -1}
    sent_low = sentence.lower()

    for word in sent_low.split():
        if word in mood_dict:
            count += mood_dict[word]

    print(count)
    if count > 0:
        print("The overall mood is Positive")
    elif count < 0:
        print("The overall mood is Negative")
    else:
        print("The overall mood is Neutral")

sentence = input("Enter a sentence with emojis: ")
analyze_mood(sentence)