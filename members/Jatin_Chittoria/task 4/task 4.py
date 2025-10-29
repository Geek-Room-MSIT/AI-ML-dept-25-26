import string

text = input("Enter a situation: ")
for ch in string.punctuation:
    text = text.replace(ch, "")
text = text.lower()
words = text.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
print("\nTop 3 most frequent words are:")
for word, count in sorted_words[:3]:
    print(f"{word}: {count}")
