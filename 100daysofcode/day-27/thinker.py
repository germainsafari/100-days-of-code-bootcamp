import turtle
from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

my_label = Label(text="I m a label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)


def button_click():
    new = input_sth.get()
    my_label["text"] = input_sth.get()


button = Button(text="click me", command=button_click)
button.grid(row=1, column=1)


def button_clicked():
    new = input_sth.get()
    my_label["text"] = new


button = Button(text="new button", command=button_clicked)
button.grid(row=0, column=3)

input_sth = Entry(width=10)
input_sth.grid(row=3, column=3)


window.mainloop()
