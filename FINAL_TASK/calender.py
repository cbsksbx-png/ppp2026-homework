from tkinter import *
from datetime import datetime

from functools import partial

from calender_list import file_module

global spinbox_M, spinbox_Y,buttonS


def spinbox_y_used():
    return spinbox_Y.get()

def spinbox_m_used():
    return spinbox_M.get()

def count_plus():
    current_val = int(spinbox_M.get())
    new_val = current_val + 1
    if new_val > 12:
        new_val = 1
    spinbox_M.delete(0, END)
    spinbox_M.insert(0, new_val)


def count_minus():
    current_val = int(spinbox_M.get())
    new_val = current_val - 1
    if new_val < 1:
        new_val = 12
    spinbox_M.delete(0, END)
    spinbox_M.insert(0, new_val)

def clear_button():
    for i in range(6):
        for j in range(7):
            buttons[f'D{i}-{j}'].config(text='', command= "")

def button_a_used():
    year = int(spinbox_y_used())
    month = int(spinbox_m_used())
    day = str(f'{year}-{month}-01')
    date_obj = datetime.strptime(day,"%Y-%m-%d")

    day_idx = date_obj.weekday()

    i = 0
    if month in (1, 3, 5, 7, 8, 10, 12):
        i = 31
    elif month in (4, 6, 9, 11):
        i = 30
    elif month == 2:
        # 2월은 윤년 계산
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            i = 29
        else:
            i = 28

    if day_idx == 0:
        clear_button()
        for a in range(6):
            buttons[f'D0-{1 + a}'].config(text=a + 1, command=partial(file_module, f'{year}-{month}-{a + 1}'))
        for b in range(7):
            buttons[f'D1-{b}'].config(text=b + 7, command=partial(file_module, f'{year}-{month}-{b + 7}'))
        for c in range(7):
            buttons[f'D2-{c}'].config(text=c + 14, command=partial(file_module, f'{year}-{month}-{c + 14}'))
        for d in range(7):
            buttons[f'D3-{d}'].config(text=d + 21, command=partial(file_module, f'{year}-{month}-{d + 21}'))
        for e in range(i - 27):
            buttons[f'D4-{e}'].config(text=e + 28, command=partial(file_module, f'{year}-{month}-{e + 28}'))

    elif day_idx == 1:
        clear_button()
        for a in range(5):
            buttons[f'D0-{2 + a}'].config(text=a + 1, command=partial(file_module, f'{year}-{month}-{a + 1}'))
        for b in range(7):
            buttons[f'D1-{b}'].config(text=b + 6, command=partial(file_module, f'{year}-{month}-{b + 6}'))
        for c in range(7):
            buttons[f'D2-{c}'].config(text=c + 13, command=partial(file_module, f'{year}-{month}-{c + 13}'))
        for d in range(7):
            buttons[f'D3-{d}'].config(text=d + 20, command=partial(file_module, f'{year}-{month}-{d + 20}'))
        for e in range(i - 26):
            buttons[f'D4-{e}'].config(text=e + 27, command=partial(file_module, f'{year}-{month}-{e + 27}'))

    elif day_idx == 2:
        clear_button()
        for a in range(4):
            buttons[f'D0-{3 + a}'].config(text=a + 1, command=partial(file_module, f'{year}-{month}-{a + 1}'))
        for b in range(7):
            buttons[f'D1-{b}'].config(text=b + 5, command=partial(file_module, f'{year}-{month}-{b + 5}'))
        for c in range(7):
            buttons[f'D2-{c}'].config(text=c + 12, command=partial(file_module, f'{year}-{month}-{c + 12}'))
        for d in range(7):
            buttons[f'D3-{d}'].config(text=d + 19, command=partial(file_module, f'{year}-{month}-{d + 19}'))
        for e in range(i - 25):
            buttons[f'D4-{e}'].config(text=e + 26, command=partial(file_module, f'{year}-{month}-{e + 26}'))

    elif day_idx == 3:
        clear_button()
        for a in range(3):
            buttons[f'D0-{4 + a}'].config(text=a + 1, command=partial(file_module, f'{year}-{month}-{a + 1}'))
        for b in range(7):
            buttons[f'D1-{b}'].config(text=b + 4, command=partial(file_module, f'{year}-{month}-{b + 4}'))
        for c in range(7):
            buttons[f'D2-{c}'].config(text=c + 11, command=partial(file_module, f'{year}-{month}-{c + 11}'))
        for d in range(7):
            buttons[f'D3-{d}'].config(text=d + 18, command=partial(file_module, f'{year}-{month}-{d + 18}'))
        for e in range(i - 24):
            buttons[f'D4-{e}'].config(text=e + 25, command=partial(file_module, f'{year}-{month}-{e + 25}'))

    elif day_idx == 4:
        clear_button()
        for a in range(2):
            buttons[f'D0-{5 + a}'].config(text=a + 1, command=partial(file_module, f'{year}-{month}-{a + 1}'))
        for b in range(7):
            buttons[f'D1-{b}'].config(text=b + 3, command=partial(file_module, f'{year}-{month}-{b + 3}'))
        for c in range(7):
            buttons[f'D2-{c}'].config(text=c + 10, command=partial(file_module, f'{year}-{month}-{c + 10}'))
        for d in range(7):
            buttons[f'D3-{d}'].config(text=d + 17, command=partial(file_module, f'{year}-{month}-{d + 17}'))
        if month == 2:
            for e in range(i - 23):
                buttons[f'D4-{e}'].config(text=e + 24, command=partial(file_module, f'{year}-{month}-{e + 24}'))
        elif month != 2:
            for e in range(7):
                buttons[f'D4-{e}'].config(text=e + 24, command=partial(file_module, f'{year}-{month}-{e + 24}'))
            if i - 28 > 0:
                for f in range(i - 30):
                    buttons[f'D5-{f}'].config(text=f + 31, command=partial(file_module, f'{year}-{month}-{f + 31}'))

    elif day_idx == 5:
        clear_button()
        for a in range(1):
            buttons[f'D0-{6 + a}'].config(text=a + 1, command=partial(file_module, f'{year}-{month}-{a + 1}'))
        for b in range(7):
            buttons[f'D1-{b}'].config(text=b + 2, command=partial(file_module, f'{year}-{month}-{b + 2}'))
        for c in range(7):
            buttons[f'D2-{c}'].config(text=c + 9, command=partial(file_module, f'{year}-{month}-{c + 9}'))
        for d in range(7):
            buttons[f'D3-{d}'].config(text=d + 16, command=partial(file_module, f'{year}-{month}-{d + 16}'))
        if month == 2:
            for e in range(i - 22):
                buttons[f'D4-{e}'].config(text=e + 23, command=partial(file_module, f'{year}-{month}-{e + 23}'))
        elif month != 2:
            for e in range(7):
                buttons[f'D4-{e}'].config(text=e + 23, command=partial(file_module, f'{year}-{month}-{e + 23}'))
            if i - 28 > 0:
                for f in range(i - 29):
                    buttons[f'D5-{f}'].config(text=f + 30, command=partial(file_module, f'{year}-{month}-{f + 30}'))

    elif day_idx == 6:
        clear_button()
        for a in range(7):
            buttons[f'D0-{a}'].config(text=a + 1, command=partial(file_module, f'{year}-{month}-{a + 1}'))
        for b in range(7):
            buttons[f'D1-{b}'].config(text=b + 8, command=partial(file_module, f'{year}-{month}-{b + 8}'))
        for c in range(7):
            buttons[f'D2-{c}'].config(text=c + 15, command=partial(file_module, f'{year}-{month}-{c + 15}'))
        for d in range(7):
            buttons[f'D3-{d}'].config(text=d + 22, command=partial(file_module, f'{year}-{month}-{d + 22}'))
        if month == 2:
            for e in range(i - 28):
                buttons[f'D4-{e}'].config(text=e + 29, command=partial(file_module, f'{year}-{month}-{e + 29}'))
        elif month != 2:
            for e in range(i - 28):
                buttons[f'D4-{e}'].config(text=e + 29, command=partial(file_module, f'{year}-{month}-{e + 29}'))

def main():
    global spinbox_M, spinbox_Y, buttons
    today = datetime.today()

    root = Tk()

    root.title("calendar")
    root.geometry("250x280")

    frame1 = Frame(root, relief="solid", bd=2)
    year = IntVar(value=today.year)
    spinbox_Y = Spinbox(frame1, from_=2003, to=2026, width=5, command=spinbox_y_used, textvariable=year)
    spinbox_Y.grid(row=0, column=3)
    Label(frame1, text="년").grid(row=0, column=4)

    Button(frame1, text="<-", width=3, command=count_minus).grid(row=1, column=0)
    month = IntVar(value=today.month)
    spinbox_M = Spinbox(frame1, from_=1, to=12, width=2, command=spinbox_m_used, textvariable=month)
    spinbox_M.grid(row=1, column=3)
    Label(frame1, text="월", width=3).grid(row=1, column=4)
    Button(frame1, text='변경', command=button_a_used).grid(row=1, column=5)

    Button(frame1, text="->", width=3, command=count_plus).grid(row=1, column=6)

    days = ['일', '월', '화', '수', '목', '금', '토']
    for i in range(7):
        Button(frame1, text=days[i], width=3).grid(row=2, column=i)

    buttons = {}
    for r in range(6):
        for c in range(7):
            btn = Button(frame1, text='', width=3)
            btn.grid(row=3 + r, column=c)
            buttons[f'D{r}-{c}'] = btn
            if c == 0:
                buttons[f'D{r}-{c}'].config(bg='red')
            if c == 6:
                buttons[f'D{r}-{c}'].config(bg='blue')

    Button(frame1, text='Exit', command=frame1.quit).grid(row=9, column=6)

    frame1.pack(side="left", fill="both", expand=True)

    Label(frame1)

    root.mainloop()


if __name__ == "__main__":
    main()
