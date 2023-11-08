from data_file import data
from art import logo, vs
import random

start = input("do you want to play Higher Lower game? enter yes or no: ")
if start == "yes".lower():
    is_game = True
else:
    is_game = False
    quit()

# while is_game:



if is_game:
    for i in range(len(data)):
        print(logo)
        compare_A = data[i]["name"]
        print(compare_A + " " + "a " + data[i]["description"])
        compare_B = data[i + 1]["name"]
        print(vs)
        print(compare_B + " " + "a " + data[i + 1]["description"])
        score = 0
        answer = input("who has many followers? type 'A' or 'B'")
        if answer == "A" and data[i]["follower_count"] > data[i+1]["follower_count"]:
            score += 1
            print("you are right! " + data[i]["name"] + " has more followers than " + data[i + 1]["name"])
            print("your current score is " + str(score))
        elif answer == "B".upper() and data[i]["follower_count"] < data[i+1]["follower_count"]:
            print("you are wrong! Game over")
            print(score)
            quit()
        else:
            print("choose the right answer!!")
    else:
        print("game o")

else:
    is_game = False



