from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My snake game")
screen.bgcolor("black")
screen.tracer(0)
starting_position = [(0, 0), (-20, 0), (-40, 0)]
segment = []
for position in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segment.append(new_segment)
screen.update()
game_is_on = True
while game_is_on:

    for seg in segment:
        seg.forward(30)








screen.exitonclick()