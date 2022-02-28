from tkinter import * 

count_click = 0

def click_count():
    global count_click
    count_click = count_click + 1
    label_click.config(text=count_click)



root = Tk()

root.title("Cookie Clicker")
root.iconbitmap('img/cookie(1).ico')
root.geometry("600x600")
root.minsize(600, 600)
root.maxsize(600, 600)
root.resizable(0, 0)


cookie = PhotoImage(file='img/cookiebtn.png')

canvas = Canvas(
    root,
    width=720,
    height=600,
    highlightthickness=0,
    bg='brown'
)

label_click = Label(
    root,
    font=("Arial",20),
    bg='brown',
    text=count_click
)
btn_cookie = Button(
    bg='brown',
    borderwidth=0,
    image=cookie,
    command=click_count
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