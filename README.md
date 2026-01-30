# AI-ML-dept-25-26

## PYTHON REVISION

### TASK 1: Emoji Mood Analyzer (Beginner – Strings & Dicts)

**Goal:**  
Take a sentence as input and decide if it's positive, negative, or neutral based on words/emojis.

**Concepts Revised:**  
Strings, dictionaries, loops, conditionals, basic logic.

**Hint:**
- Make a dict like `{"love": 1, "😍": 1, "hate": -1, "😫": -1}`
- Loop through keys, and count how many appear in the sentence.
- Compare positive vs negative counts.

**Starter Template:**
```python
sentence = input("Enter a sentence with emojis: ")

mood_dict = {"love": 1, "😍": 1, "happy": 1, "hate": -1, "😫": -1, "sad": -1}

# TODO: initialize positive = 0, negative = 0
# TODO: loop through mood_dict keys and count how many are in sentence
# TODO: compare and print result like "Overall Mood: Positive/Negative/Neutral"
```

### TASK 2: Random Story Generator (Intermediate – Lists & Random)

**Goal:**  
Generate a random 2-line funny story by mixing random characters, places, and actions.

**Concepts Revised:**  
Lists, random module, string formatting.

**Hint:**
- Create 3–4 lists: characters, places, objects, actions.
- Use `random.choice()` to pick one from each and build a sentence.
- Run it multiple times for new results.

**Starter Template:**
```python
import random

characters = ["a sleepy panda", "an alien", "a pirate", "a robot"]
places = ["in the jungle", "on Mars", "at a tech fest", "in the library"]
objects = ["a laptop", "a treasure map", "a sandwich", "a phone"]
actions = ["started coding", "fell asleep", "built a rocket", "lost their WiFi"]

# TODO: use random.choice() to pick one from each list
# TODO: print something like:
# "Once upon a time, ___ found ___ ___ and ___!"
```

**Bonus Twist:**  
Add an input:  
```python
how_many = int(input("How many stories do you want? "))
```
and loop that many times.

### TASK 3: Treasure Hunt Game (Logic & Loops)

**Goal:**  
Hide a treasure randomly in a list of 5 places. Player guesses until they find it.

**Concepts Revised:**  
Loops, conditionals, user input, indexing, random.

**Hint:**
- Create a list: `["_", "_", "_", "_", "_"]`
- Randomly choose a treasure position (index).
- Let the user guess (1–5) until they find it.
- After each guess, tell them "too left" or "too right".

**Starter Template:**
```python
import random

map = ["_", "_", "_", "_", "_"]
treasure = random.randint(0, 4)

found = False

while not found:
    guess = int(input("Guess the position (1-5): ")) - 1
    
    # TODO: check if guess == treasure
    # TODO: print hints like "Too left!" or "Too right!"
    # TODO: replace guessed position with "O" for tried spots
    # TODO: print current map after each guess

print("You found the treasure! 🏆")
```

### TASK 4: Word Frequency Finder (Intermediate – Strings, Dicts & Loops)

**Goal:**  
Take a paragraph and show which words appear most often. It helps revise loops, dictionaries, and sorting — and quietly builds the mindset of finding “important features” in text data.

**Concepts Revised:**  
Strings, dicts, loops, sorting.

**Instructions:**  
1. Ask the user for a paragraph.  
2. Convert everything to lowercase and remove punctuation.  
3. Split into words.  
4. Count how many times each word appears.  
5. Show the top 3 most frequent words.

**Starter Template:**
```python
text = input("Enter a paragraph: ")

# TODO: clean punctuation like . , ! ?

# TODO: split text into words

# TODO: use a dictionary to count each word

# TODO: sort by count and print top 3 words
```

**Hint:**  
You can use `.replace()` to remove punctuation and `sorted(dict.items(), key=lambda x: x[1], reverse=True)` to sort.

### TASK 5: Trend Tracker (Intermediate – Lists & Math)

**Goal:**  
Given a list of numbers (like daily temperatures or stock prices), detect if the trend is rising, falling, or stable — and estimate the next value.

**Concepts Revised:**  
Lists, math operations, loops, averages, conditionals.

**Instructions:**  
1. Start with a predefined list like `[30, 31, 33, 34, 35]`.  
2. Find differences between consecutive values.  
3. Compute the average of those differences.  
4. Predict the next number using that average difference.  
5. Print the trend and the predicted value.

**Starter Template:**
```python
values = [30, 31, 33, 34, 35]

# TODO: find consecutive differences

# TODO: calculate avg_diff

# TODO: detect trend: rising / falling / stable

# TODO: predict next_value = values[-1] + avg_diff

print(f"Predicted next value: {next_value}")
```

### TASK 6: Smart Sensor Classifier (Advanced – OOP Basics)

**Goal:**  
Simulate how AI models classify inputs — but using simple object-oriented design. Each “sensor” will analyze a numeric value and label it as Low, Medium, or High.

**Concepts Revised:**  
Classes, objects, methods, conditionals, modular logic.

**Instructions:**  
Create a class `Sensor` that:  
- Has an `__init__` method that takes a sensor name and threshold values.  
- Has a `classify(value)` method that prints whether the reading is low, medium, or high.  
- Create 2–3 sensors (like temperature, humidity) and test them on random values.

**Starter Template:**
```python
import random

class Sensor:
    def __init__(self, name, low, high):
        # TODO: store parameters as attributes
        pass

    def classify(self, value):
        # TODO: write logic to print whether value is Low/Medium/High
        pass

# Example usage
temp_sensor = Sensor("Temperature", 20, 30)
humidity_sensor = Sensor("Humidity", 40, 60)

for i in range(3):
    temp_sensor.classify(random.randint(10, 40))
    humidity_sensor.classify(random.randint(20, 80))
```

**Hint:**  
This is like how an ML model uses decision boundaries to classify inputs — only here, you define the rules manually instead of learning them!

### TASK 7: Mini ML Workflow Simulator (Advanced – Modular OOP)

**Goal:**  
Build a simplified 3-file project that mimics how an AI pipeline works — data input, model logic, and prediction. Each file plays the role of a different part of a machine learning system.

**Concepts Revised:**  
OOP, modular programming, file imports, logic structuring.

**Instructions:**  
You will create three Python files:  

**data_loader.py**  
- Define a class `DataLoader` that reads a list of numbers (e.g., `[12, 15, 18, 20, 22]`).  
- Add a method `get_data()` that returns that list.  

**simple_model.py**  
- Define a class `SimpleModel` with:  
  - A method `train(data)` that computes the average.  
  - A method `predict(x)` that compares `x` to the average and returns "Above Average" or "Below Average".  

**main.py**  
- Import both classes.  
- Create objects of `DataLoader` and `SimpleModel`.  
- Train the model and make predictions for a few test values.  
- Print the results nicely.

**Starter Templates:**  

**data_loader.py**
```python
class DataLoader:
    def __init__(self):
        # TODO: store a list of numbers (e.g., [12, 15, 18, 20, 22])
        pass

    def get_data(self):
        # TODO: return the data list
        pass
```

**simple_model.py**
```python
class SimpleModel:
    def __init__(self):
        # TODO: initialize any needed variables (like avg)
        pass

    def train(self, data):
        # TODO: compute and store the average of data
        pass

    def predict(self, x):
        # TODO: return "Above Average" or "Below Average" based on avg
        pass
```

**main.py**
```python
from data_loader import DataLoader
from simple_model import SimpleModel

# TODO: Load data
loader = DataLoader()
data = loader.get_data()

# TODO: Train model
model = SimpleModel()
model.train(data)

# TODO: Test predictions
test_values = [10, 20, 25]
for val in test_values:
    result = model.predict(val)
    print(f"Value {val} → {result}")
```

**Hint:**  
This structure mirrors how real AI systems work:  
- `data_loader.py` → handles data ingestion  
- `simple_model.py` → represents your model  
- `main.py` → runs the full pipeline
