text = input("Enter a paragraph: ").lower()

for p in [".", ",", "!", "?", ";", ":"]:
    text = text.replace(p, "")

words = text.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)

print("\nTop 3 most frequent words:")
for word, count in sorted_words[:3]:
    print(f"{word}: {count}")
