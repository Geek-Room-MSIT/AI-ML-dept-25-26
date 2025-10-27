msg = input("Give me the input sentence: ")

mood_dict = {"love" : 1, "😍" : 1, "happy" : 1, "hate": -1, "😫" : -1, "sad" : -1, "good": 1, "bad":-1}

n=0
p=0


for i in mood_dict:
    if i in msg:
        if mood_dict[i] == 1:
            p+=1
        if mood_dict[i] == -1:
            n+=1


print("Total positive words in the sentence are: ",p)
print("Total negative words in the sentence are: ",n)

if p == n:
    print("Overall mood : Neutral")
elif p>n:
    print("Overall mood : Positive")
else:
    print("Overall mood : Negative")
