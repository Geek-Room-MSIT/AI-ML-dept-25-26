text = input("Enter the paragraph: ")
new_text= text.lower()
punctuation = ".,!?;:'\"-()"

for i in punctuation :
    new_text= new_text.replace(i,"")

words = new_text.split()

word_count= {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word]=1

sort= sorted(word_count.items(),key= lambda x: x[1], reverse=True)

print("Top 3 words are: ")
for i in range(3):
    word,count= sort[i]
    print(f"{word} - {count} times")    
