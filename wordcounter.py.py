import tkinter as tk
from tkinter import ttk

def count_words(text):
    words = text.split()
    return len(words)

def on_count_button_click():
    text = text_entry.get("1.0", tk.END)
    word_count = count_words(text)
    result_label.config(text=f"Word count: {word_count}")

# Create the main window
root = tk.Tk()
root.title("Word Counter")

# Create and place the text entry widget
text_entry = tk.Text(root, wrap="word", width=50, height=10)
text_entry.pack(padx=10, pady=10)

# Create and place the count button
count_button = ttk.Button(root, text="Count Words", command=on_count_button_click)
count_button.pack(pady=10)

# Create and place the result label
result_label = ttk.Label(root, text="Word count: 0")
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
