import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.geometry("1600x900")

def hello():
    messagebox.showinfo('hello', 'world')

button = tk.Button(app, text="button", command=hello)
button.pack()

app.mainloop()