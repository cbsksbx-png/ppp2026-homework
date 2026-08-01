from functools import partial
from tkinter import *

def open_file(filename):
    try:
        with open('file' + '/' + filename, "r", encoding="utf-8") as f:
            text.delete(1.0, END)
            text.insert(END, f.read())
    except FileNotFoundError:
        pass


def save_file(filename):
    with open('file' + '/' + filename, "w", encoding="utf-8") as f:
        f.write(text.get(1.0, END))


def file_module(filename):
    global text
    root = Tk()
    root.title(f'{filename}')
    root.geometry("600x400")

    menubar = Menu(root)
    root.config(menu=menubar)

    file_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="파일", menu=file_menu)

    file_menu.add_command(label="저장", command=partial(save_file, filename))

    text = Text(root, font=("맑은 고딕", 12))
    text.pack(fill=BOTH, expand=True)

    open_file(filename)

    root.mainloop()
