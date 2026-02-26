import tkinter as tk
from tkinter import messagebox
import random

#Arrays for questions and answers
questions = ["Was ist ein\nCyber-Physisches System (CPS)?",      #1
             "Welche drei\nHauptbestandteile hat ein CPS?",      #2
             "Welche Aufgaben\nhaben Sensoren in CPS?",          #3
             "Welche Aufgaben\nhaben Aktoren in CPS?",           #4
             "Warum ist Echtzeitfähigkeit\nbei CPS wichtig?",    #5
             "Nenne typische\nMerkmale von CPS",                 #6
             "Nenne Beispiele\nfür Cyber-Physische Systeme",     #7
             "Welche Rolle spielen\nCPS in Industrie 4.0?",      #8
             "welche Vorteile\nbieten CPS?",                     #9
             "Welche Herausforderungen\ngibt es bei CPS?"]       #10

answers = ["Ein System, das physische Prozesse mit Software und Netzwerken verbindet und in Echtzeit steuert.",      #1
           "Sensoren, Aktoren und eingebettete Systeme (Software + Hardware).",                                      #2
           "Sie erfassen physische Daten wie Temperatur, Druck oder Bewegung.",                                      #3
           "Sie setzen digitale Steuerbefehle in physische Aktion um (z.B. Motor starten.)",                         #4
           "Damit das System sofort auf Veränderungen reagieren kann.",                                              #5
           "Vernetzung, Autonomie, Echtzeitfähigkeit, Adaptivität, Sicherheit.",                                     #6
           "Smart Home, autonomes Fahren, Smart Grid, Industrie 4.0 Anlagen.",                                       #7
           "Sie sind die technologische Grundlage für intelligente, vernetzte Fabriken.",                            #8
           "Effizienzsteigerung, Automatisierung, Flexibilität, bessere Datennutzung.",                              #9
           "IT-Sicherheit, Datenschutz, hohe Komplexität und Kosten."]                                              #10

rand = list(range(0, 10)) # list of integers from 0 to 9
random.shuffle(rand)
count = 0

def q_and_a():
    global count
    if(count<=9):
        messagebox.showinfo("Answer",answers[rand[count]])
        count = count + 1
    else: 
        count = 0
    label.config(text=questions[rand[count]])

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
root.mainloop()
