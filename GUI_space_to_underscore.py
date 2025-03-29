import tkinter as tk
from tkinter import messagebox as mg
import pyperclip

def main(a):
    a = a.replace(' ', '_').replace(':', '_')
    pyperclip.copy(a)
    mg.showinfo('Information', 'Your result has been copied')

win = tk.Tk()
win.geometry('500x500')  # Set window size
win.resizable(0, 0)  # Prevent window resizing

# Button to copy clipboard content
clipbutton = tk.Button(win, text='Clipboard', foreground='black', font=('Arial', 30),
                       command=lambda: main(pyperclip.paste()))
clipbutton.place(x=0, y=0, width=200, height=100)

# Entry for manual input
manual_input = tk.Entry(win, font=('Arial', 45))
manual_input.place(x=0, y=150, width=400, height=100)

# Submit button to process input
submit_button = tk.Button(win, text='Submit', foreground='black', font=('Arial', 30),
                          command=lambda: main(manual_input.get()))
submit_button.place(x=0, y=250, width=200, height=100)

win.mainloop()