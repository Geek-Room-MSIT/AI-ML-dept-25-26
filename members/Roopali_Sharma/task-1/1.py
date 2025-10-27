# EMOJI MOOD ANALYZER
mood={
    "happy":1,
    "sad":-1,
    "bad":-1,
    "okok":0,
    "tired":-1,
    "loving":1,
    "hectic":-1,
    "fun":1,
    "angry":-1,
    "anxious":-1,
    "sick":-1,
    "yummy":1,
    "good":1,
    "fine":0,
    "sleep":-1,
    "sleepy":-1,
    "ill":-1,
    "hate":-1,
    "excited":1,
    '😥' :-1,
    '🙂' :1,
    '😋' :1,
    '😓' :-1,
    '😍' :1,
    '🥰' :1,
    '🥱':-1,
}
count=0
sentence=input("How's your mood 🤗?");
for key,value in mood.items():
    if key in sentence:
        count+=value
if count==0:
    print("Mood is Neutral😐")       
if count>0:
    print("Mood is Good 😇")       
if count<0:
    print("Mood is Bad 😢")    
