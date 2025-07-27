# Console Wordle - Python Edition

A simple **Wordle** clone built with Python for the command line. Guess the hidden 5-letter word within 6 attempts, and get feedback after each guess!

---

## 🎮 Features

- A word is randomly chosen from a word list (`words.txt`)
- The user has 6 attempts to guess the 5-letter word
- After each guess, the program outputs:
  - ✅ for correct letters in the correct position
  - 🟨 for correct letters in the wrong position
  - ⬛ for incorrect letters

Letter counting is handled precisely to avoid over-highlighting duplicate letters.

---

## 📂 File Structure

wordle-console-game/  
├── main.py # Main game loop  
├── word_list.py # Word list loader  
├── letter_count_dictionary.py # Tracks letter frequencies in target word  
├── words.txt # List of valid words (one per line)  
└── README.md # You're reading it!  

## Sample Gameplay

Guess the 5-letter word: trace
⬛🟨⬛⬛✅

Guess the 5-letter word: tease
✅✅⬛⬛✅

Guess the 5-letter word: taste
✅✅✅✅✅
Well done, you guessed the word TASTE. It only took you 2 attempts
