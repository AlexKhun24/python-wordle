import random
from word_list import dictionary
from letter_count_dictionary import dictionary_initialization as init
num_attempts = 6

word_choice = (random.choice(dictionary)).upper()

#Initial guess
user_guess = input ("Guess the 5-letter word: ")
while len(user_guess) != 5:
    user_guess = input ("Make sure your guess is 5 letters. Try again: ")

user_guess = user_guess.upper()

if word_choice == user_guess:
    print("✅✅✅✅✅")
    exit(0)
else:
    num_attempts -= 1

while num_attempts >= 0:
    letters_and_count = init(word_choice)
    print(f"letters_and_count dictionary: {letters_and_count}")
    for i in range(5):
        if user_guess[i] == word_choice[i]:
            print("✅", end="")

        elif user_guess[i] != word_choice[i] and user_guess[i] in letters_and_count:
            print("🟨", end="")

        elif user_guess[i] != word_choice[i]:
            print("⬛", end="")

    if num_attempts == 0:
        break
    user_guess = input("\nGuess the 5-letter word: ")
    while len(user_guess) != 5:
        user_guess = input("Make sure your guess is 5 letters. Try again: ")

    user_guess = user_guess.upper()
    num_attempts -= 1
    if word_choice == user_guess:
        print("✅✅✅✅✅")
        exit(0)

print("\nYou lose.")