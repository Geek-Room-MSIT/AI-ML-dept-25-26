import tkinter as tk
import random

characters = ["a sleepy panda", "an alien", "a pirate", "a robot"]
places = ["in the jungle", "on Mars", "at a tech fest", "in the library"]
objects = ["a laptop", "a treasure map", "a sandwich", "a phone"]
actions = ["started coding", "fell asleep", "built a rocket", "lost their WiFi"]

def generate_story():
    line1 = f"{random.choice(characters)} {random.choice(actions)} {random.choice(objects)} {random.choice(places)}."
    line2 = f"{random.choice(characters)} {random.choice(actions)} {random.choice(objects)} {random.choice(places)}."
    story_text.set(f"{line1}\n{line2}")

window = tk.Tk()
window.title("Random Story Generator")
window.geometry("600x400")
window.resizable(False, False)
window.config(bg="#f0f0f0")

header = tk.Label(window, text="Random Story Generator", font=("Comic Sans MS", 20, "bold"), bg="#f0f0f0", fg="#333")
header.pack(pady=15)

story_text = tk.StringVar()
story_label = tk.Label(window, textvariable=story_text, font=("Arial", 14), bg="#ffffff", fg="#222",
                       width=60, height=6, wraplength=550, justify="center", bd=4, relief="ridge")
story_label.pack(pady=20)

generate_btn = tk.Button(window, text="Generate Story", command=generate_story,
                         font=("Arial", 14, "bold"), bg="#4CAF50", fg="white",
                         activebackground="#45a049", relief="raised", bd=3, width=20)
generate_btn.pack(pady=10)

window.mainloop()
