#Play Hangman with a friend. One is inserting the word and the pther player guesses.

import random
import os
from hangman_art import logo, stages

def clear_terminal():
    os.system('clear' if os.name == 'posix' else 'cls')

chosen_word = (input("Anna sana: ").lower())

clear_terminal()

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
  guess = input("Arvaa kirjain: ").lower()
  clear_terminal()
  print (logo)
  if guess not in guessed_letters:
    guessed_letters.append(guess)
    i = 0
    for letter in chosen_word:
      if letter == guess:
        display[i] = guess
        correct_answer = True
      i += 1
    if correct_answer == False:
      print(guess.upper() + " ei ole sanassa")
      lives -= 1
    else:
      print("Hienoa!")
  else:
    print("Sanoit jo kirjaimen " + guess.upper())
#if the displayed word is complete, user wins, otherwise, they lose.
if '_' not in display:
  print(stages[lives])
  print(f"{' '.join(display).upper()}\n")
  print("VOITIT!")
else:
  print(stages[lives])
  print(f"{' '.join(display).upper()}\n")
  print("Peli ohi! Oikea sana olisi ollut " + chosen_word.upper())
exit()
