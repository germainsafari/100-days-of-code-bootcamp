import random
import time
import pandas
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# window.minsize(600, 600)
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="card_front.png")
canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 100, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 40, "italic"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=1, column=1, columnspan=2)

data = pandas.read_csv("french_words.csv")
data_dict = data.to_dict(orient="records")
print(data_dict)


def flash_card():
    new_word = random.choice(data_dict)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=new_word["French"])
    print(new_word["French"])


wrong = PhotoImage(file="wrong.png")
button1 = Button(image=wrong, command=flash_card)
button1.grid(row=2, column=1)

right = PhotoImage(file="right.png")
button2 = Button(image=right, command=flash_card)
button2.grid(row=2, column=2)
flash_card()
window.mainloop()
