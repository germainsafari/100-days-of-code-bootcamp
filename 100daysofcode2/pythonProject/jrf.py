def play_game():
  word = "heaven"
  max_trials = 3
  trials = 0

  while trials < max_trials:
    guess = input("Guess the word: ")
    if guess == word:
      print("You guessed correctly! You won the game.")
      return
    else:
      trials += 1
      print(f"Incorrect guess. You have {max_trials - trials} trial(s) left.")

  print("You have used all your trials. Better luck next time!")

play_game()
