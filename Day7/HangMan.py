# Day 7: For & While loops, IF/ELSE statements, Strings, Lists, Range function, Modules etc...
# HangMan Project

import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Initialize placeholder
placeholder = ""
for position in range(word_length):
    placeholder += "_"

print(logo)
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"**************************** {lives}/6 LIVES LEFT ****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            game_over = True
            print(f"*********************** IT WAS {chosen_word}! YOU LOSE **********************")

    if "_" not in display:
        game_over = True
        print("**************************** YOU WIN ****************************")

    # Only add the guess to correct_letters once after checking
    if guess not in correct_letters:
        correct_letters.append(guess)

    print(stages[lives])
