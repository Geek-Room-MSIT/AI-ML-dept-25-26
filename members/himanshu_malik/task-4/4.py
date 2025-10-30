import string

text = input("Enter a paragraph: ")



for ch in string.punctuation:
    text = text.replace(ch, "")

text=text.lower()
word_count = {}

words = text.split()
for word in words:
    if word in word_count:
        word_count[word] +=1
    else:
        word_count[word] = 1

a = sorted(word_count.items(), key= lambda x: x[1], reverse=True)

print("\nThe most common words in the paragraph are:")

for word, count in a[:3]:
    print (f"{word} showed up {count} times")
