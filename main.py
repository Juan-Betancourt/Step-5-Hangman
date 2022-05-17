from replit import clear
import random
import hangman_words
import hangman_art

from hangman_words import word_list 
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo, stages
print(logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    user_selection = input("Guess a letter: ").lower()

    clear()
  
    if user_selection in display:
      print(f"You have already entered {user_selection} please try again")
    else:
    #Check user_selection letter
      for position in range(word_length):
          letter = chosen_word[position]
          if letter == user_selection:
              display[position] = letter

    #Checking if the user is wrong.
    if user_selection not in chosen_word:
        print(f"You guessed the letter {user_selection} which is not in the word. You lost a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(chosen_word)

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
        print(chosen_word)
  
    print(stages[lives])