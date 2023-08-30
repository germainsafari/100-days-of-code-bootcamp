from flask import Flask
import random
players = ["Jokic", "Jimmy", "Murray"]
player = random.choice(players)
app = Flask(__name__)


@app.route('/')
def home():
    return "<h1> Guess a player who won the MVP finals </h1>"\
            "<img src='https://media.giphy.com/media/MCU2fU2QaxHqDdrhJr/giphy-downsized-large.gif'/>"
@app.route('/<string:guess>')
def nba_player(guess):
    if guess == player:
        return "<h1>you got it right, Jokic is a Viking</h1>"\
        "<img src='https://media.giphy.com/media/ftSalHoEma5EtzulYE/giphy.gif'/>"
    else:
        return "<h1>Go to sing, BA is not your game</h1>"\
        "<img src='https://media.giphy.com/media/9GJ34PEVM5JnCkfPPf/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)
