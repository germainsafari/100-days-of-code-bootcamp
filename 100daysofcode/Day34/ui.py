from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("My quiz")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)
        self.label = Label(text="score")
        self.label.grid(row=0,column=1)
        self.canvas = Canvas(width=300, height=300, bg="white")
        self.question_text = self.canvas.create_text(150, 100, text="some info", fill=THEME_COLOR)
        self.canvas.grid(row=1, column= 0)
        right = PhotoImage("true.png")
        self.right_button = Button(image=right)
        self.right_button.grid(row=2, column=1)
        wrong = PhotoImage("false.png")
        self.wrong_button = Button(image=wrong)
        self.wrong_button.grid(row=2, column=1)
        self.window.mainloop()
