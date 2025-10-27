text = input("Enter a paragraph: ")

for ch in [",",".","?","!",";",":","'",'"']:
    text=text.replace(ch,"")

text=text.lower()

words=text.split()

word_count={}

for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1

sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
print(sorted_words)
