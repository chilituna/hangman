
import random

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#select random word from list
word_list = ["konttero", "akvaariokala", "lastenvessa", "kissankello", "humma", "kikkoman"]
chosen_word = random.choice(word_list)

#create a list of blanks for the chosen word and set lives to begin
display = []
for i in range(len(chosen_word)):
  display.append('_')
lives = 6

#create a list to stored already guessed letters
guessed_letters = []

print (logo)

while '_' in display and lives > 0:
  print(stages[lives])
  print(f"{' '.join(display)}\n")
  correct_answer = False
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
      lives -= 1
  else:
    print("You already gave that word.")
if '_' not in display:
  print(stages[lives])
  print(f"{' '.join(display)}\n")
  print("You win!")
else:
  print(stages[lives])
  print(f"{' '.join(display)}\n")
  print("You lose! The correct word would have been " + chosen_word)
exit()
