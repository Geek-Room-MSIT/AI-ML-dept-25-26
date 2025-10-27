#Take a paragraph and show which words appear most often.

# sentence = Are you, Ama, really okay? Because okay, okay, okay, everyone keeps asking are you Ama okay, ? That’s just strange… but maybe you are okay. i asked, "Ama, are you okay okay okay?" But nobody says why the okay keeps coming up. Every time there’s a dot, every time there’s an exclamation mark! And when you find a comma, there’s an okay again, okay, okay, okay — so much okay! Explain to me, um, why there is always okay and dot and exclamation, but no one explains why okay is there, okay, okay, okay. In fact, even when you say cool, it all returns to okay again!

def count_word_occurrences(sentence):
    a = sentence.lower()
    b=list(a)
    c=list(a)
    i = 0
    while i<=len(c):
        try:
            if "." in b :
                b.remove(".")
            elif "," in b:
                b.remove(",")
            elif("!") in b:
                b.remove("!")
            elif("?") in b:
                b.remove("?")
        except ValueError:
            pass
        i+=1
    a = ''.join(b)
    b = a.split()
    list1 = []
    occur = []
    count = 0
    for word in a.split():
        if word not in list1:
            for i in a.split():
                if i == word:
                    count = count + 1
            occur.append(count)
            list1.append(word)
            count = 0
        else:
            continue
    occurance=max(occur)
    index = occur.index(occurance)
    maxoccur = list1[index]
    print(f"The most occuring word in the Sentence is '{maxoccur}' which have repeated {occurance} times")

sentence = input("Enter the sentence : ")
count_word_occurrences(sentence)