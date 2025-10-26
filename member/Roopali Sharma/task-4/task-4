# Word Frequency Finder 
para=input("Enter a paragraph: ")
para=para.lower()
para=para.removeprefix(",")
para=para.removeprefix(".")
para=para.removeprefix("'")
para=para.removeprefix("!")
text=para.split()
words={} #dictionary
for a in text :
    if a in words:
        words[a]+=1
    else:
        words[a]=1
top=sorted(words.items(), key=lambda x: x[1], reverse=True)
print("-" * 35)
if len(top) >= 1:
    word1, count1 = top[0]
    print(f"1st most common word: {word1} (Count: {count1})")
if len(top) >= 2:
    word2, count2 = top[1]
    print(f"2nd most common word: {word2} (Count: {count2})")
if len(top) >= 3:
    word3, count3 = top[2]
    print(f"3rd most common word: {word3} (Count: {count3})")
