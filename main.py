import random
from word_list import dictionary

num_attempts = 6

word_choice = (random.choice(dictionary)).upper()
print(word_choice)

#Initial guess before loop
user_guess = input ("Guess the word: ")
user_guess = user_guess.upper()

if word_choice == user_guess:
    print("✅✅✅✅✅")
    exit(0)
else:
    for i in range(5):
        if user_guess[i] == word_choice[i]:
            print("✅", end="")
        elif user_guess[i] != word_choice[i]:
            print("⬛", end="")