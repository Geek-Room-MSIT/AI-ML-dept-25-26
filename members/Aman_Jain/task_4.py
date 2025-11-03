text = input("Enter a paragraph: ")

for p in [".", ",", "!", "?", ":", ";", "’", "'", '"']:
    text = text.replace(p, "")

words = text.lower().split()
word_count = {}

for w in words:
    word_count[w] = word_count.get(w, 0) + 1

sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
top_three = sorted_words[:3]

print("Top 3 most frequent words:")
for word, count in top_three:
    print(f"{word}: {count}")
