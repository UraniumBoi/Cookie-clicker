from tkinter import * 
from customtkinter import *

count_click = 0

def click_count():
    global count_click
    count_click = count_click + 1
    label_click.config(text=count_click)


def reset():
    global count_click
    count_click = 0
    label_click.config(text=count_click)

root = CTk()

root.title("Cookie Clicker")
root.iconbitmap('img/cookie(1).ico')
root.geometry("600x600")
root.minsize(600, 600)
root.maxsize(600, 600)
root.resizable(0, 0)


cookie = PhotoImage(file='img/cookiebtn.png')
cook = PhotoImage(file='img/cookieicon.png')

canvas = Canvas(
    root,
    width=720,
    height=600,
    highlightthickness=0,
    bg='brown'
)
reset_btn = CTkButton(
    text="",
    width=35,
    height=35,
    fg_color='brown',
    bg_color='brown',
    borderwidth=0,
    image=cook,
    command=reset
)
label_click = Label(
    root,
    font=("Arial",20),
    bg='brown',
    text=count_click
)
btn_cookie = CTkButton(
    fg_color='brown',
    hover_color='brown',
    text="",
    borderwidth=0,
    image=cookie,
    command=click_count
)
canvas.create_window(
    250,
    3,
    anchor=NW,
    window=reset_btn
)
canvas.create_window(
    300,
    0,
    anchor=NW,
    window=label_click
)
canvas.create_window(
    50,
    50,
    anchor=NW,
    window=btn_cookie

)

canvas.pack(expand=YES)


root.mainloop()