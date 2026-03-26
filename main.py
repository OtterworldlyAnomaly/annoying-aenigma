import tkinter as tk
from tkinter import messagebox
import random
import toml
# libraries imports


q_and_a = dict()
# Dictionaries for questions and answers

rand = list(range(0, q_and_a.items())) # list of integers from 0 to 9
random.shuffle(rand)
count = 0
# random number generator to shuffle q and a

def add_to_qna():
    question = input("Enter a question"); answer = input("Enter the answer") # 

# Create the main application window
root = tk.Tk()
root.title("Simple Python GUI")
root.geometry("300x120")  # Width x Height

# Create and place a label
label = tk.Label(root, text=questions[rand[count]], font=("Arial", 12))
label.pack(pady=5)

# Create and place a button
greet_button = tk.Button(root, text="Next", font=("Arial", 12),command=q_and_a)
greet_button.pack(pady=10)

# Start the Tkinter event loop
if __name__ == "__main__":   
    root.mainloop()
