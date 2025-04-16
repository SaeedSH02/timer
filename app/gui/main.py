import tkinter as tk
from tkinter import messagebox
from app.core.timer import countdown


def start_timer():
    try:
        minutes = int(entry.get())
        countdown(minutes, label)
    except ValueError:
        messagebox.showerror("Error, please enter a valid integer.")


def build_gui():
    global entry, label

    root = tk.Tk()
    root.title("Countdown timer")
    root.geometry("400x300")

    tk.Label(root, text="Duration (minutes):").pack(pady=10)
    entry = tk.Entry(root, width=25)
    entry.pack(pady=5)

    tk.Button(root, text="Start timer", command=start_timer).pack(pady=10)
    label = tk.Label(root, text="", font=("Helvetica", 16))
    label.pack(pady=40)



    root.mainloop()