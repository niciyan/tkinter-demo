import tkinter as tk
from tkinter import messagebox

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        self.root = tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("800x600")
        self.title('TestApp')

        for i in range(10):
            self.frame = tk.Frame(self.root)
            self.frame.pack()
            self.button = tk.Button(self.frame, text="My name is Chau.", fg="red", command=self.hello)
            self.button.pack(side=tk.LEFT)

            self.label = tk.Label(self.frame, text="ok")
            self.label.pack(side=tk.LEFT)

        # self.button = tk.Button(self.root, text="save")
        # self.button.pack()
        #
        # self.label = tk.Label(self.root, text="ok")
        # self.label.pack()

    def hello(self):
        messagebox.showinfo("message", "My name is Chau")

app = App()
app.mainloop()
