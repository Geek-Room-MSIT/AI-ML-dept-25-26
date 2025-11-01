text = input("Enter a paragraph: ")
text = text.lower()
for ch in [".", ",", "!", "?", ";", ":", "'", '"']:
    text = text.replace(ch, "")
words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print("The 3 most frequent words:")
used_words = sorted(word_count, key=word_count.get, reverse=True)[:3]

for word in used_words:
    print(f"{word}: {word_count[word]} times")
