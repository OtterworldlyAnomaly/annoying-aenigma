import tkinter as tk
from tkinter import messagebox
import random
import toml
# libraries imports


sample_dict = {"Paul": "Phoenix",
           "Asuka": "Kazama",
           "Jin": "Kazama",
           "Jun": "Kazama",
           "Kazuya": "Mishima",
           "Heihachi": "Mishima",
           "Steve": "Fox",
           "Miary": "Zo",
           }
# Dictionaries for questions and answers

rand = list(range(0,len(sample_dict.items()))) # list of integers from 0 to 9
random.shuffle(rand)
count = 0
# random number generator to shuffle q and a

def add_to_dict():
    first_v = input("Enter first value"); second_v = input("Enter second value")
    sample_dict[first_v] = second_v

# Create the main application window
root = tk.Tk()
root.title("Simple Python GUI")
root.geometry("300x120")  # Width x Height

# Create and place a label
label = tk.Label(root, text="test", font=("Arial", 12))
label.pack(pady=5)

# Create and place a button
# greet_button = tk.Button(root, text="Next", font=("Arial", 12))
# greet_button.pack(pady=10)

text = tk.Text(root)
text.insert('1.0',sample_dict)
text.pack(pady=4)

# Start the Tkinter event loop
if __name__ == "__main__":   
    root.mainloop()