
dict1 = {'love': 1, 'like': 1, 'adore': 1, 'admire': 1, 'admiration': 1, 'joy': 1, 'fun': 1, 'confident': 1, 'confidence': 1, 'elated': 1, 'hope': 1, 'happy': 1, 'excited': 1, 'excitement': 1, 'delighted': 1, 'sad': -1, 'hate': -1, 'disgusting': -1, 'disgusted': -1, 'gloomy': -1, 'angry': -1, 'anger': -1, 'fear': -1, 'guilty': -1, 'guilt': -1, 'shameful': -1, 'shame': -1, 'ashamed': -1, 'disappointed': -1, 'disappointment': -1, 'lonely': -1, 'jealous': -1, 'jealousy': -1, 'frustated': -1, 'frustation': -1, 'anxious': -1, 'fear': -1, 'scared': -1, 'afraid': -1, '😆': 1, '😄': 1, '🙂': 1, '🥰': 1, '😍': 1, '😊': 1, '😞': -1,'🙁': -1, '😭': -1, '😠': -1, '😩': -1}

s = input("Enter a sentence with emojis: ")
pos=0
neg=0

for i in dict1.keys():
    if i in s:
        if dict1[i] == 1:
            pos+=1
        else:
            neg+=1

import time
print("Calculating...")
time.sleep(1)
print("Overall mood: ",end='')

if pos>neg:
    print("POSITIVE")
elif pos<neg:
    print("NEGATIVE")
else:
    print("NEUTRAL")
