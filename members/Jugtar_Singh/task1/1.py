emotion_values = {
    # Positive emotions
    "happy": 1,
    "joyful": 1,
    "excited": 1,
    "content": 1,
    "grateful": 1,
    "hopeful": 1,
    "relaxed": 1,
    "proud": 1,
    "confident": 1,
    "enthusiastic": 1,
    "inspired": 1,
    "cheerful": 1,
    "satisfied": 1,
    "optimistic": 1,
    "loving": 1,
    "peaceful": 1,
    "energetic": 1,

    # Neutral emotions
    "neutral": 0,
    "indifferent": 0,
    "calm": 0,
    "bored": 0,
    "curious": 0,
    "tired": 0,
    "pensive": 0,
    "observant": 0,
    "contemplative": 0,
    "reluctant": 0,
    "uninterested": 0,

    # Negative emotions
    "sad": -1,
    "angry": -1,
    "frustrated": -1,
    "anxious": -1,
    "depressed": -1,
    "disappointed": -1,
    "lonely": -1,
    "jealous": -1,
    "scared": -1,
    "guilty": -1,
    "ashamed": -1,
    "embarrassed": -1,
    "hopeless": -1,
    "irritated": -1,
    "resentful": -1,
    "hurt": -1,
    "worried": -1,

    '😥' :-1,
    '🙂' :1,
    '😋' :1,
    '😓' :-1,
    '😍' :1,
    '🥰' :1,
    '🥱':-1,
}


sentence = input("Enter a sentence describing your mood: ")
c1 = 0 
c2 =0
moods = sentence.split()
print(moods)
for mood in moods:
    if mood in emotion_values:
        value = emotion_values[mood]
        if value > 0:
            c1 += 1
        else:
            c2 -= 1

overall_mood = c1 + c2 

if overall_mood > 0:
    print("Your mood is Positive 😊")
elif overall_mood < 0:
    print("Your mood is Negative 😞")
else:
    print("Your mood is Neutral 😐")