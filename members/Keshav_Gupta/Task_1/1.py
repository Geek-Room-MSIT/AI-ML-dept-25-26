
sentiment = {
    "love": 1, "good": 1, "great": 1, "happy": 1, "nice": 1, "best": 1, "like": 1,
    "hate": -1, "bad": -1, "terrible": -1, "sad": -1, "worst": -1, "angry": -1,
    "😊": 1, "😃": 1, "👍": 1,
    "😢": -1, "😞": -1, "👎": -1,
}

negations = {"not", "no", "never", "don't"}

def mood(sentence):
    score = 0
    words = sentence.lower().split()
    
    for i in range(len(words)):
        clean = words[i].strip('.,!?')
        if clean in sentiment:
            score += sentiment[clean]
            if i > 0 and words[i-1] in negations:
                score *= -1
    
    # Check emojis
    for emoji in sentiment:
        if emoji in sentence:
            score += sentiment[emoji]
    
    if score > 0:
        return "positive"
    elif score < 0:
        return "negative"
    else:
        return "neutral"


# Test
sentences = [
    "I love this! 😊",
    "This is terrible",
    "Not bad",
    "Great day 👍",
]

for s in sentences:
    print(f"{s} → {mood(s)}")
    
    
input_sentence = input("Enter a sentence: ")
print(f"The mood of the sentence is: {mood(input_sentence)}")