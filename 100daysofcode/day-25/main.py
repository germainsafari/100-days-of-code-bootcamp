import turtle
import pandas

screen = turtle.Screen()
screen.title("US states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states = pandas.read_csv("50_states.csv")
all_states = states.state.to_list()
# guess = ""
# score = 0
# correct_guesses = []
# game_is_on = True
# while game_is_on:
#     if guess in states["state"]:
#         answer_state = screen.textinput(title="Guess a state", prompt="what is the other state").lower()
#         correct_guesses.append(guess)
#         score += 1
guessed_states = []
answer_state = screen.textinput(title="Guess a state", prompt="what is the other state").lower()
if answer_state in all_states:
    guessed_states.append(answer_state)
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    states_match = states[states.state == answer_state]
    t.goto(int(states_match.x), int(states_match.y))
    t.write(states_match.state)



screen.exitonclick()

# data = pandas.read_csv("weather_data.csv")
# data_to_list = data["temp"].to_list()
# n =  sum(data_to_list)/len(data_to_list)
# print(n)
# print(data[data.day == "Monday"])

# monday = data[data.day == "monday"]
# print(monday.condition)
# mon_temp = int(monday.temp)
# cel = mon_temp * 5 / 9 + 32
