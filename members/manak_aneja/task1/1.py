mood_index={"love":1, "hate":-1, "😍":1, "😫":-1}

def analyze_mood():
    sent=input("write a sentence with emojis: ")
    words=sent.split()
    positive=0
    negative=0
    for word in words:
        if word in mood_index:
            if word.lower()=="love" or word=="😍":
                positive+=1
            elif word.lower()=="hate" or word=="😫":
                negative-=1
    mood_score=positive+negative
    if mood_score>0:
        print("overall mood: positive")
    elif mood_score<0:
        print("overall mood: negative")
    else:
        print("overall mood: neutral")
analyze_mood()