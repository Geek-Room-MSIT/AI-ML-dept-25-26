sentence=input("Enter your sentence:")

mood_dict={
    "happy": 1,
    "sad":-1,
    "😃":1,
    "😄":1,
    "🥲":-1,
    "😞":-1,
    "😔":-1,
    "bad":-1,
    "good": 1,
    "hurt": -1,
}
positive=0
negative=0 

for m in mood_dict:
    if m in sentence:
        if mood_dict[m]== 1:
            positive+=1
        elif mood_dict[m]== -1:
            negative+=1

if positive>negative:
    print("Overall Mood: Happy")
elif positive==negative:
    print("Overall Mood: Neutral")
else:
    print("Overall Mood: Sad")
