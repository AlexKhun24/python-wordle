import random
from word_list import dictionary

num_attempts = 6

word_choice = (random.choice(dictionary)).upper()

#list to store letters in word for checking
choice_letters = []
for letter in word_choice:
    if letter not in choice_letters:
        choice_letters.append(letter)

print(word_choice)
print(choice_letters)

#Initial guess before loop
user_guess = input ("Guess the word: ")
user_guess = user_guess.upper()

if word_choice == user_guess:
    print("✅✅✅✅✅")
    exit(0)
else:
    while num_attempts > 0:
        for i in range(5):
            if user_guess[i] == word_choice[i]:
                print("✅", end="")
            elif user_guess[i] != word_choice[i] and user_guess[i] in choice_letters:
                print("🟨", end="")

            elif user_guess[i] != word_choice[i]:
                print("⬛", end="")
        num_attempts -= 1

        user_guess = input("\nGuess the word: ")
        user_guess = user_guess.upper()
        if word_choice == user_guess:
            print("✅✅✅✅✅")
            exit(0)