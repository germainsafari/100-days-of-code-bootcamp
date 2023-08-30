import turtle
from tkinter import *

window = Tk()
window.title("My first GUI program")

window.config(padx=20, pady=20)


def value():
    new_value = int(input_sth.get())
    my_label["text"] = new_value * 1.6


button = Button(text="calculate", command=value)
button.grid(row=3, column=2)

input_sth = Entry(width=10)
input_sth.grid(row=0, column=1)

my_label = Label(text="0")
my_label.grid(row=1, column=2)

my_labels = Label(text="Miles")
my_labels.grid(row=0, column=3)

my_label1 = Label(text="is equal to")
my_label1.grid(row=1, column=1)

my_label2 = Label(text="km")

my_label2.grid(row=1, column=3)

# entry = Entry(width=30)
# entry.insert(END, string="0")

window.mainloop()


