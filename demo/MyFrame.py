import tkinter as tk


class MyFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=800, height=500, bg="gray")
        self.master = master

        # menu
        menubar = tk.Menu(self)
        menu_file = tk.Menu(menubar, tearoff=False)
        menu_file.add_command(label="test", command=lambda text="    ":self.update_text(text))
        menu_file.add_command(label="exit", command=self.master.destroy)
        menubar.add_cascade(label="file", menu=menu_file)
        self.master.config(menu=menubar)

        # prefix part
        self.frame = tk.Frame(master=self,)
        self.frame.pack(anchor=tk.W, padx=10, pady=10)

        self.prefix_label = tk.Label(master=self.frame, text="Prefix")
        self.prefix_label.pack(side=tk.LEFT, padx=10, pady=10)

        self.prefix_entry = tk.Entry(master=self.frame, text="> ")
        self.prefix_entry.insert(tk.END, '> ')
        self.prefix_entry.pack(side=tk.LEFT, padx=10, pady=10)

        a = """Ctrl + Y -> change background color to yellow
b
c
d
        """
        self.usage_label = tk.Label(master=self, text=a)
        self.usage_label.pack(side=tk.RIGHT, padx=10, pady=10)

        self.frame2 = tk.Frame(master=self)
        self.frame2.pack(anchor=tk.W, padx=10, pady=10)

        self.text_box = tk.Text(master=self.frame2, height=10)
        self.text_box.insert(1.0, '--example\naa\nbb')
        self.text_box.pack(fill=tk.X, padx=10, pady=10)

        self.text_box2 = tk.Text(master=self.frame2, height=10)
        self.text_box2.pack(fill=tk.X, padx=10, pady=10)

        self.button2 = tk.Button(master=self.frame2, text="update", command=self.update_text_with_entry)
        self.button2.pack(side=tk.RIGHT, anchor=tk.NE)

        self.update_text_with_entry()

        self.button = tk.Button(master=self.frame2, text="button", command=self.read_text)
        self.button.pack(side=tk.RIGHT, anchor=tk.NE)

        self.master.bind('<Control-Key-q>', lambda event, text="    ": self.update_text(text))
        self.master.bind('<Control-Key-e>', lambda event, text="> ": self.update_text(text))
        self.master.bind('<Control-Key-y>', lambda event, color="yellow": self.update_frame_color(color))

        self.pack(padx=10, pady=10, ipadx=10, ipady=10)
        # self.pack_propagate(0)


    def read_text(self):
        # print(self.text_box.get('1.0', 'end-1c')
        for line in self.text_box.get('1.0', 'end-1c').splitlines():
            print('> ', line)

    def update_text_bind(self, event):
        self.update_text("    ")

    def update_text_with_entry(self):
        self.update_text(self.prefix_entry.get())

    def update_text(self, text):
        self.text_box2.config(state=tk.NORMAL)
        self.text_box2.delete(1.0, tk.END)
        # for line in self.text_box.get('1.0', 'end-1c'):
        #     self.text_box2.insert(line)
        self.text_box2.insert(1.0,
                              "".join([text + line + '\n' for line in self.text_box.get('1.0', 'end-1c').splitlines()]))

        self.text_box2.config(state=tk.DISABLED)

    def update_frame_color(self, color):
        self.frame["bg"] = color

app = tk.Tk()
app.geometry("1600x900")
frame = MyFrame(master=app)
frame.mainloop()
