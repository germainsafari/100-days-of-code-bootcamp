import random

choices = ["rock", "paper", "scissors"]
computer = random.choices(choices)
player = None
print(computer)
while player not in choices:
    player = input("rock, paper or scissors?").lower()
if player == computer:
    print("player:", player)
    print("computer:", computer)
    print("Tie")
elif player == "rock":
    if computer == "paper":
        print("computer:", computer)
        print("player:", player)
        print("you lose")
    if computer == "scissors":
        print("computer:", computer)
        print("player:", player)
        print("you win")
elif player == "paper":
    if computer == "rock":
        print("computer:", computer)
        print("player:", player)
        print("you win")
    if computer == "scissors":
        print("computer:", computer)
        print("player:", player)
        print("you lose")
elif player == "scissors":
    if computer == "rock":
        print("computer:", computer)
        print("player:", player)
        print("you lose")
    if computer == "scissors":
        print("computer:", computer)
        print("player:", player)
        print("you win")
