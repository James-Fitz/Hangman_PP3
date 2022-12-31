# **Hangman**

Am I Responsive Image

<br>

**Live deployed application can be found** [HERE](https://hangman-james-fitz.herokuapp.com/)  

<br>

## **Introduction**

Hangman is a simple word game that requires the player to guess the missing letters in an unknown word where the length of the word is known.
The strategy most commonly implemented while playing the game of hangman is to guess the most commomnly seen letters in the English language first and try to work out the answer from there.
Often players will begin by guessing the vowels, A,E,I,O and U, which gives a good starting point to discovering the word.

This project is a terminal based hangman game that is written completely using the Python programming language.
User input is accepted through number or letter entries into the command line of the terminal.

I decided to allow the user to choose a category of words to pick from (animals, brands or countries), and also a difficulty level to choose from (easy: 5 letter word, intermediate: 6 letter word, or hard: 7 letter word.)

These words are stored on an external google spreadsheet which makes it very simple to add or remove words from the game.

Oncde the user begins a new game, they must input one letter at a time to guess the hidden word.
If the user guesses a letter correctly, the letter will be revealed.
If the user guesses incorrectly, a body part will be added to the hangman image and the player must guess again.
The game ends when either the player guesses all the letters correctly or the hangman is fully formed and the player loses.

When the game is over, the results will be displayed and the sub menu will be displayed to the user to return to the main menu or quit the game.

<br>

## **Table of Contents**
- [**Hangman**](#hangman)
  - [**Introduction**](#introduction)
  - [**Table of Contents**](#table-of-contents)
