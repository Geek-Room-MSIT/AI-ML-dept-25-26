import re
from collections import Counter

def top_words(text, n=3):
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    return Counter(words).most_common(n)

def main():
    try:
        text = input("Enter text: ").strip()
        if not text:
            raise ValueError("Input cannot be empty.")
        result = top_words(text)
        if not result:
            raise ValueError("No valid words found.")
        for word, freq in result:
            print(word, freq)
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Unexpected error:", e)

if __name__ == "__main__":
    main()
