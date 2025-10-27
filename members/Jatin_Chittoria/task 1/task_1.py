mood_dict = {
    "😊": "happy",
    "😢": "sad",
    "😠": "angry",
    "😎": "cool",
    "😂": "laughing",
    "😱": "scared",
    "😴": "tired"
}

user_input = input("Enter the emojis: ")
for emoji in user_input:
    if emoji in mood_dict:
        print(f"The mood for {emoji} is: {mood_dict[emoji]}")
    else:
        print(f"{emoji} is an unknown mood")
      
