sentence=input("Kindly enter the sentence :- ")    
mood_dict = {
        "love": 1, "happy": 1, "joy": 1, "like": 1, "amazing": 1,"😍": 1, "😂": 1, "😊": 1, "👍": 1,
        "hate": -1, "sad": -1, "angry": -1, "terrible": -1, "dislike": -1,"😫": -1, "😭": -1, "😠": -1, "👎": -1
    }

score = 0

for word, value in mood_dict.items():
  if word in sentence.lower():
    score += value
    
   
if score > 0:
  print("The sentence ",sentence," is positive 😃 by the score of ",score)
elif score < 0:
  print("The sentence ",sentence ," is negative 😔 by the score of ",score)
else:
  print("The sentence ",sentence," is neutral 😐 by the score of ",score)

