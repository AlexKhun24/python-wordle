import random
from word_list import dictionary
from letter_count_dictionary import dictionary_initialization as init

def main():
    num_attempts = 0
    word_choice = (random.choice(dictionary)).upper()
    #Initial guess
    user_guess = input ("Guess the 5-letter word: ")
    while len(user_guess) != 5:
        user_guess = input ("Make sure your guess is 5 letters. Try again: ")

    user_guess = user_guess.upper()

    if word_choice == user_guess:
        print("✅✅✅✅✅")
        print(f"Well done, you guessed the word {word_choice}. It only took you {num_attempts} attempts")
        exit(0)
    else:
        num_attempts += 1

    while num_attempts <= 6:
        #initialize letters_and_count to reset letter count values per guess
        letters_and_count = init(word_choice)
        square_output = ["⬛", "⬛", "⬛", "⬛", "⬛"]
        #print(f"letters_and_count dictionary: {letters_and_count}") #test line
        for i in range(5):
            if user_guess[i] == word_choice[i]:
                square_output[i] = "✅"
                letters_and_count[user_guess[i]] -= 1

        for i in range(5):
            if user_guess[i] != word_choice[i] and user_guess[i] in letters_and_count and letters_and_count.get(user_guess[i]) != 0:
                square_output[i] = "🟨"
                letters_and_count[user_guess[i]] -= 1

        print("".join(square_output))

        if num_attempts == 6:
            break
        user_guess = input("\nGuess the 5-letter word: ")
        while len(user_guess) != 5:
            user_guess = input("Make sure your guess is 5 letters. Try again: ")

        user_guess = user_guess.upper()
        num_attempts += 1
        if word_choice == user_guess:
            print("✅✅✅✅✅")
            exit(0)

    print(f"\nYou lose. The word was {word_choice}.")

if __name__ == "__main__":
    main()