sentence = input("Enter a sentence with emojis: ").lower()

sentiment_dict = {
    # Positive words and emojis
    "happy": 1, "smiling": 1, "love": 1, "great": 1, "good": 1,
    "amazing": 1, "awesome": 1, "fantastic": 1, "excellent": 1,
    "beautiful": 1, "grateful": 1, "joy": 1, "wonderful": 1,
    "excited": 1, "fun": 1, "cool": 1, "blessed": 1, "thankful": 1,
    "nice": 1, "peaceful": 1, "positive": 1, "motivated": 1,
    "😊": 1, "😄": 1, "😁": 1, "😍": 1, "🥰": 1, "😎": 1, "👍": 1,
    "🤩": 1, "😇": 1, "💖": 1, "🎉": 1, "✨": 1, "💪": 1, "❤️": 1,

    # Negative words and emojis
    "sad": -1, "depressed": -1, "angry": -1, "bad": -1,
    "terrible": -1, "horrible": -1, "hate": -1, "upset": -1,
    "lonely": -1, "disappointed": -1, "tired": -1, "bored": -1,
    "pain": -1, "cry": -1, "frustrated": -1, "worried": -1,
    "anxious": -1, "stressed": -1, "hopeless": -1,
    "😢": -1, "😭": -1, "😡": -1, "😠": -1, "👎": -1, "😞": -1,
    "😔": -1, "💔": -1, "🙁": -1, "😩": -1, "😖": -1, "😒": -1,

    # Neutral words
    "okay": 0, "fine": 0, "neutral": 0, "normal": 0,
    "maybe": 0, "alright": 0, "meh": 0, "average": 0,
    "😐": 0, "😶": 0, "🤔": 0,
}

negations = {"not", "no", "never", "n't"}

words = sentence.split()
score = 0

for i, word in enumerate(words):
    if word in sentiment_dict:       
        if i > 0 and words[i - 1] in negations:
            value = -sentiment_dict[word]  
            print(f"Found 'not {word}': {value}") #for debugging
        else:
            value = sentiment_dict[word]
            print(f"Found '{word}': {value}") #for debugging
        score += value

if score > 0:
    sentiment = "Positive 😊"
elif score < 0:
    sentiment = "Negative 😔"
else:
    sentiment = "Neutral 😐"

print("Overall Sentiment:", sentiment)
