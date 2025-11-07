import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Information", "Button was clicked!")
root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry("300x200")
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=50, padx=100, fill='x', expand=True)
root.mainloop()