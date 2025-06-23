import tkinter as tk
from tkinter import ttk
import re

# --- Password Strength Logic ---
def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[@$!%*?&]", password):
        score += 1

    return score

def get_strength_feedback(score):
    if score <= 2:
        return "Weak", "red"
    elif score == 3:
        return "Moderate", "orange"
    else:
        return "Strong", "green"

# --- Toggle Password Visibility ---
def toggle_password():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        toggle_btn.config(text='Show')
    else:
        password_entry.config(show='')
        toggle_btn.config(text='Hide')

# --- Event: On Typing ---
def on_key_release(event=None):
    pwd = password_var.get()
    score = check_password_strength(pwd)
    status, color = get_strength_feedback(score)
    result_label.config(text=f"Strength: {status}", foreground=color)
    progress['value'] = score * 20  # out of 100

# --- UI Setup ---
root = tk.Tk()
root.title("🔐 Password Strength Checker")
root.geometry("400x200")
root.resizable(False, False)

password_var = tk.StringVar()

title_label = ttk.Label(root, text="Enter your password", font=("Segoe UI", 14))
title_label.pack(pady=10)

frame = ttk.Frame(root)
frame.pack()

password_entry = ttk.Entry(frame, textvariable=password_var, show="*", width=30, font=("Segoe UI", 12))
password_entry.pack(side="left", padx=(0, 5))
password_entry.bind("<KeyRelease>", on_key_release)

toggle_btn = ttk.Button(frame, text="Show", command=toggle_password)
toggle_btn.pack(side="right")

result_label = ttk.Label(root, text="Strength: ", font=("Segoe UI", 12))
result_label.pack(pady=10)

progress = ttk.Progressbar(root, length=300, mode='determinate', maximum=100)
progress.pack()

# Run the App
root.mainloop()
