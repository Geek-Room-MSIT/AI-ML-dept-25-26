text = input("Enter a paragraph: ")
for ch in [".", ",", "!", "*", "@", "#", "&"]:
  text = text.replace(ch,"")
text = text.lower()
words = text.split()
count = {}
for i in words:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
sorted_words = sorted(count.items(), key=lambda x: x[1], reverse=True)
res = []
x= min(3, len(sorted_words))
for i in range(x):
    res.append(sorted_words[i][0]) 
print(res)