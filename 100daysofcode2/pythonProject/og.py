unknown_land = "heaven"
guess = ""
guess_limit = 3
guess_count = 0
out_of_guesses = False
while guess != unknown_land and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("enter the word : ")
        guess_count += 1
        print()
    else:
        out_of_guesses = True
if out_of_guesses:
    print("out of guesses, you lose")
print("you win")