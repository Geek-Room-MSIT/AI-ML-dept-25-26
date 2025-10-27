import tkinter as tk
from tkinter import ttk

def analyze_mood(sentence):
    mood_dict = {
        "love": 2, "like": 1, "happy": 1, "good": 1, "awesome": 2, "great": 2, "😍": 2,
        "amazing": 2, "hate": -2, "bad": -1, "angry": -2, "sad": -1, "😫": -2, "😡": -2, "😭": -1
    }

    sentence = sentence.lower()
    score = sum(sentence.count(word) * value for word, value in mood_dict.items())

    if score > 0:
        mood = "😊 Positive Mood"
        color = "#ADD8E6"
    elif score < 0:
        mood = "😞 Negative Mood"
        color = "#FF8C94"
    else:
        mood = "😐 Neutral Mood"
        color = "#FFD3B6"

    result_label.config(text=f"Score: {score}\nOverall Mood: {mood}", bg=color, fg="#333333")

def on_analyze():
    text = entry.get().strip()
    if text:
        analyze_mood(text)
    else:
        result_label.config(text="Please enter a sentence!", bg="#FFD3B6", fg="#333333")

window = tk.Tk()
window.title("Mood Analyzer")
window.geometry("500x350")
window.resizable(False, False)
window.config(bg="#f7f7f7")

header = tk.Label(window, text="Mood Analyzer", font=("Helvetica", 20, "bold"), bg="#f7f7f7", fg="#333")
header.pack(pady=15)

input_frame = tk.Frame(window, bg="#f7f7f7")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Enter your sentence:", font=("Arial", 12), bg="#f7f7f7").pack(anchor="w")


entry_style = ttk.Style()
entry_style.configure("TEntry", padding=6, relief="flat", font=("Arial", 12))

entry = ttk.Entry(input_frame, width=50, style="TEntry")
entry.pack(pady=5)


entry.insert(0, "Type your sentence here...")
def on_entry_click(event):
    if entry.get() == "Type your sentence here...":
        entry.delete(0, "end")
def on_focusout(event):
    if entry.get() == "":
        entry.insert(0, "Type your sentence here...")
entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focusout)

analyze_btn = tk.Button(window, text="Analyze Mood", command=on_analyze,
                        bg="#4CAF50", fg="white", font=("Arial", 12, "bold"),
                        activebackground="#45a049", relief="raised", bd=3, width=20)
analyze_btn.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 12, "bold"), width=45, height=4, bg="#f7f7f7", bd=2, relief="sunken")
result_label.pack(pady=15)

window.mainloop()
