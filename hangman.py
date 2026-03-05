import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)
lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for i in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"******{lives}/6 LIVES LEFT******")
    guess = input("Guess a letter:").lower()

    if guess in correct_letters:
        print("You've already guessed")
    display = ""
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display +=chosen_word[i]
            correct_letters.append(guess)
        elif chosen_word[i] in correct_letters:
            display +=chosen_word[i]
        else:

             display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guesses {guess}, that's not in the word. You lose a life ")

        if lives == 0:
            game_over = True
            print(f"******IT WAS {chosen_word}! YOU LOSE******")

    if "_" not in display:
        game_over = True
        print("You win!")


    print(stages[lives])
