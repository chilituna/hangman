
import random
from hangman_art import logo, stages
from hangman_words import word_list

#select random word from list
chosen_word = random.choice(word_list)

#create a list of blanks for the chosen word
display = []
for i in range(len(chosen_word)):
  display.append('_')

#create a list to store already guessed letters
guessed_letters = []

#set lives and start the game
lives = 6
print (logo)

#loop until the word is complete or all lives are gone
#draw the stage and guessed word
while '_' in display and lives > 0:
  print(stages[lives])
  print(f"{' '.join(display).upper()}\n")
  correct_answer = False
  #ask for letter - if included, replace in the displayed word - if not, reduce life - if already guessed, inform user
  guess = input("Guess a letter: ").lower()
  if guess not in guessed_letters:
    guessed_letters.append(guess)
    i = 0
    for letter in chosen_word:
      if letter == guess:
        display[i] = guess
        correct_answer = True
      i += 1
    if correct_answer == False:
      print(guess.upper() + " is not in the word.")
      lives -= 1
  else:
    print("You already gave that letter. Try again")
#if the displayed word is complete, user wins, otherwise, they lose.
if '_' not in display:
  print(stages[lives])
  print(f"{' '.join(display).upper()}\n")
  print("You win!")
else:
  print(stages[lives])
  print(f"{' '.join(display).upper()}\n")
  print("You lose! The correct word would have been " + chosen_word)
exit()
