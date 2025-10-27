#Task 1: Emoji Mood Analyser
import string
mood_dict = { "love": 1, "😍": 1, "happy": 1, "😊": 1, "😀": 1, "😂": 1, "😎": 1,
              "🥰": 1, "😄": 1, "😆": 1, "😃": 1, "😺": 1, "🤗": 1, "🎉": 1, "✨": 1, "❤️ ": 1,
              "hate": -1, "😫": -1, "sad": -1, "😢": -1, "😭": -1, "😥": -1,
              "😞": -1, "😔": -1, "😟": -1, "😿": -1, "💔": -1, "🖤": -1, "☹️": -1,
              "angry": -1, "😡": -1, "🤬": -1}
positive=negative=0
sentence= input("Enter sentence with emojis:")
#Loop 1 to analyse mood by dividing sentence in words
for k in sentence.split():
  i=k.strip(string.punctuation)
  if(mood_dict.get(i.lower())==1):
     positive+=1
  elif(mood_dict.get(i.lower())==-1):
     negative+=1
  else: #Loop 2 to check if words have emojis without space eg:"😥😢"
    for j in i:
       if(mood_dict.get(j.lower())==1):
          positive+=1
       elif(mood_dict.get(j.lower())==-1):
          negative+=1
if(positive>negative):
    print("Overall Mood: Happy😊")
elif(negative>positive):
    print("Overall Mood: Negative😞")
else:
    print("Overall Mood: Neutral😐")

