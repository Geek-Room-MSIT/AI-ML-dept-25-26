import string

text = input("Enter a paragraph: ")

for ch in string.punctuation:
    text = text.replace(ch, "")
text = text.lower()

words = text.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

#Print top 3 words
print("\nTop 3 most frequent words:")
for word, count in sorted_words[:3]:
    print(f"{word}: {count}")
