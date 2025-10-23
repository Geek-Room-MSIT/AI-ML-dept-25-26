sentence = input("Enter a sentence with emojis: ")
iterable_sentence=sentence.lower()

mood_dict = {
    # positive emotions
    "love":1, "happy":1, "great":1, "awesome":1,
    "wonderful":1,"excellent":1,"fantastic":1,
    "good":1,"amazing":1,"nice":1,
    "😍":1,"😊":1,"😄":1,"🤩":1,"😎":1,

    # negative emotions
    "hate":-1,"sad":-1,"angry":-1,"bad":-1,
    "upset":-1,"terrible":-1,"awful":-1,
    "horrible":-1,"disappointed":-1,"tired":-1,
    "😡":-1,"😞":-1,"😫":-1,"😢":-1,"😠":-1 }

positive=0
negative=0


for word,value in mood_dict.items():
    if word in iterable_sentence:   
        if value==1:
            positive+=1
        else:
            negative+=1
    else:
        continue


if positive>negative:
    print("Overall Mood: Positive")
elif negative>positive:
    print("Overall Mood: Negative")
else:
    print("Overall Mood: Neutral")
