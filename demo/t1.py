import tkinter as tk
from tkinter import filedialog
from pygments import lex
from pygments.lexers.python import PythonLexer
from pygments.token import Token

def highlight_text(event=None):
    text.tag_remove("highlight", "1.0", "end")
    for token, content in lex(text.get("1.0", "end"), PythonLexer()):
        if token in Token.Comment:
            text.tag_add("highlight", "1.0 + %dc" % content.index("#"), "1.0 + %dc" % (content.index("#") + len(content)))
            text.tag_config("highlight", foreground="blue")
        elif token in Token.Keyword or token in Token.Keyword.Constant or token in Token.Keyword.Namespace:
            start = "1.0 + %dc" % content.index()
            end = "1.0 + %dc" % (content.index() + len(content))
            text.tag_add("highlight", start, end)
            text.tag_config("highlight", foreground="blue")
        elif token in Token.Name.Builtin:
            start = "1.0 + %dc" % content.index()
            end = "1.0 + %dc" % (content.index() + len(content))
            text.tag_add("highlight", start, end)
            text.tag_config("highlight", foreground="green")
        elif token in Token.Operator or token in Token.Punctuation:
            start = "1.0 + %dc" % content.index()
            end = "1.0 + %dc" % (content.index() + len(content))
            text.tag_add("highlight", start, end)
            text.tag_config("highlight", foreground="red")

def open_file():
    file_path = filedialog.askopenfilename()
    with open(file_path, "r") as f:
        text.delete("1.0", "end")
        text.insert("end", f.read())
    highlight_text()

def save_file():
    file_path = filedialog.asksaveasfilename()
    with open(file_path, "w") as f:
        f.write(text.get("1.0", "end"))

root = tk.Tk()
root.title("テキストエディタ")

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="ファイル", menu=file_menu)
file_menu.add_command(label="開く", command=open_file)
file_menu.add_command(label="保存", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="終了", command=root.quit)

text = tk.Text(root)
text.pack()
text.bind("<KeyRelease>", highlight_text)

root.mainloop()
