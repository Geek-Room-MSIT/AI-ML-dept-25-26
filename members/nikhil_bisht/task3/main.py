
import tkinter as tk
import random

def setup_game():
    global treasure_index
    treasure_index = random.randint(0, 4)
    for i, btn in enumerate(place_buttons):
        btn.config(text="❓", bg="#87CEEB", state="normal")
    feedback_label.config(text="Guess where the treasure is hidden (1-5)!", bg="#f0f0f0", fg="#333")

def guess_place(index):# this fn will handle guess logic on clicking button
    if index == treasure_index:
        place_buttons[index].config(text="💎", bg="#FFD700")
        feedback_label.config(text="Congratulations! You found the treasure!", fg="#006400")
        for btn in place_buttons:
            btn.config(state="disabled")
    elif index < treasure_index:
        feedback_label.config(text="Too left! Try a higher number.", fg="#1E90FF")
    else:
        feedback_label.config(text="Too right! Try a lower number.", fg="#FF4500")

window = tk.Tk()
window.title("Treasure Hunt Game")
window.geometry("600x300")
window.resizable(False, False)
window.config(bg="#f0f0f0")

header = tk.Label(window, text="Treasure Hunt Game", font=("Comic Sans MS", 20, "bold"), bg="#f0f0f0", fg="#333")
header.pack(pady=15)

button_frame = tk.Frame(window, bg="#f0f0f0")
button_frame.pack(pady=20)

place_buttons = []
for i in range(5):
    btn = tk.Button(button_frame, text="❓", font=("Arial", 18, "bold"), width=4, height=2,
                    bg="#87CEEB", fg="white", command=lambda i=i: guess_place(i))
    btn.grid(row=0, column=i, padx=10)
    place_buttons.append(btn)

feedback_label = tk.Label(window, text="", font=("Arial", 14, "bold"), bg="#f0f0f0", fg="#333")
feedback_label.pack(pady=15)

reset_btn = tk.Button(window, text="Reset Game", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",
                      activebackground="#45a049", relief="raised", bd=3, width=15, command=setup_game)
reset_btn.pack(pady=10)

setup_game()
window.mainloop()
