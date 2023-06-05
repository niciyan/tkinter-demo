import tkinter as tk


app = tk.Tk()
app.geometry("1600x900")

textbox = tk.Text(app, width=30, font=("Helvetica", 15))
textbox.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

app.mainloop()