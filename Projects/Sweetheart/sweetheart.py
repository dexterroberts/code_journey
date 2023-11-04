import tkinter as tk
from tkinter import messagebox

def check_memory():
    user_input = input_text.get(1.0, "end-1c").lower()
    memory_keywords = ["parking", "lot", "wedding", "late", "present", "gift"]
    
    if any(keyword in user_input for keyword in memory_keywords):
        response_label.config(text="You remembered! It's crazy how far back that was, right? I remember you looked pretty that day, but for the last time don't ask me to recall what color dress you were wearing, haha")
    else:
        response_label.config(text="That's not quite it. Try again! Remember we were both late to an event?")

def start_program():
    welcome_label.config(text="Do you remember the very first time we met?")
    start_button.config(state="disabled")
    input_text.config(state="normal")
    submit_button.config(state="active")

# Create the main window
window = tk.Tk()
window.title("Sweetheart Coding Project")

# Welcome Message
welcome_label = tk.Label(window, text="Hi, Honey! Welcome to my coding project, 'Sweetheart!'\nI'm sure you're wondering what this simple text program could be and aren't sure what to expect...\nWell, don't worry. I put some time into this and I think you'll understand it in a minute or two! Enjoy <3", wraplength=400)
welcome_label.pack()

# Start button
start_button = tk.Button(window, text="Start", command=start_program)
start_button.pack()

# Text entry
input_text = tk.Text(window, height=10, width=40)
input_text.pack()
input_text.config(state="disabled")

# Submit button
submit_button = tk.Button(window, text="Submit", command=check_memory)
submit_button.pack()
submit_button.config(state="disabled")

# Response label
response_label = tk.Label(window, text="")
response_label.pack()

window.mainloop()
