# **Hangman**

inser Am I Responsive Image here

<br>

**Live deployed application can be found** [HERE](https://hangman-james-fitz.herokuapp.com/)  

<br>

## **Introduction**

Hangman is a simple word game that requires the player to guess the missing letters in an unknown word where the length of the word is known.
The strategy most commonly implemented while playing the game of hangman is to guess the most commomnly seen letters in the English language first and try to work out the answer from there.
Often players will begin by guessing the vowels, A,E,I,O and U, which gives a good starting point to discovering the word.

This project is a terminal based hangman game that is written completely using the Python programming language.
User input is accepted through number or letter entries into the command line of the terminal.

I decided to allow the user to choose a category of words to pick from (animals, brands or countries), and also a difficulty level to choose from (easy: 5 letter word, intermediate: 6 letter word, or hard: 7 letter word).
This allows more variety and gives the user a hint at what word they will be guessing which in turn creates a more enjoyable experience.

The random words are stored on an external google spreadsheet which makes it very simple to add or remove words from the game at any time.

Once the user begins a new game, they must input one letter at a time to guess the hidden word.
If the user guesses a letter correctly, the letter will be revealed.
If the user guesses incorrectly, a body part will be added to the hangman image and the player must guess again.
All previously guessed letters are displayed to the user.
The game ends when either the player guesses all the letters correctly or the hangman is fully formed and the player loses.

When the game is over, the results will be displayed and the sub menu will be displayed for the user to return to the main menu or quit the game.

<br>

## **Table of Contents**
- [**Hangman**](#hangman)
  - [**Introduction**](#introduction)
  - [**Table of Contents**](#table-of-contents)
  - [**UX and Design**](#ux-and-design)
  - [**Features**](#features)
  - [**Testing**](#testing)
    - [Python Linter Validation](#python-linter-validation)
    - [User Input Testing](#user-input-testing)
    - [Browser Tests](#browser-tests)
    - [Bugs and Errors](#bugs-and-errors)
  - [**Technology Used**](#technology-used)
    - [Imports](#imports)
  - [**Deployment**](#deployment)
  - [**Credits**](#credits)



## **UX and Design**  

I wanted to ensure a very clean, easy to understand and visually appealing UX for this project.
As it is a terminal based project there wasn't a lot of scope for design choice.
I implemented a simple color gradient for the background of the page to make the terminal stand out to the user.
I also centred the terminal on the window as I feel it is more appealing for the player.

The application opens to a main menu with some ASCII art displaying the Hangman title.
The selections available to the user are colored. "Play game", "Rules" and "Credits" are colored green and "Quit" is colored red.
This ensures that the user knows the 0 input will end the application.

Once the user enters 1 to play the game, they are given 3 options for category choice.
"Animals", "Brands" or "Countries".
These numbers are also colored to be more visually appealing to the user.

Once the user chooses a category they are given a choice of diificulty levels.
"Easy", "Intermediate" or "Hard".
These numbers are color coded green, yellow and red respectively as these are universally understood colors to indicate difficulty level.

Once the user has chosen the difficulty level the game screen will be displayed.
The category and difficulty choice will remain at the top of the page.
Below these, there are a number underscores denoting the amount of letters in the word.
Below the underscores, there will be an ASCII art image of a gallows, showing the player how close they are to losing.
Below the gallows the players previously guessed letters are displayed and underneath this is a player input request.

I have used red and green throughout this project to inform the user when an invalid/incorrect entry has been made and when a valid/correct entry has been made.

If a user inputs an invalid entry, an incorrect answer or loses the game, they will be given a message in red.

If the user guesses a letter correctly or wins the game, they will be given a message in green.

<details><summary>Target Audience</summary>

- This game is suitable for all age groups.
- This game was made for fans of simple word games.
- Anyone that enjoys simple terminal based games.

</details>

<details><summary>User Experience and Expectations</summary>  

- Simple game to play.
- Clear instructions and rules that are easy to understand.
- Simple design and easy navigation.
- intuative design where results and outcomes are easily identified and displayed.
- Clear indication of input errors to the user.
- Ability to see progress throughout the game, how many guesses are left, how many letters guessed correctly, whiich letters have already been guessed.
- Variety and choice for a new experience every time.
- Ability to return to the main menu at the end of the game and restart the application.

</details>

<details><summary>Flow Chart</summary>  

Insert flowchart here

</details>

<details><summary>Wireframe</summary>  

Insert wireframe here

</details>

<details><summary>Color Palette</summary>

As this is a terminal based project, there wasn't much scope for color modifications.
I added color to the terminal using colorama, and I added a simple red to cyan gradient background to the body of the page using css.

</details>

## **Features** 
<details><summary>Main Menu</summary>     

Add main menu image here

</details>

<details><summary>Rules Page</summary>     

Add rules image here

</details>

<details><summary>Credits Page</summary>     

Add Credits image here

</details>

<details><summary>Sub Menu</summary>  

Add sub menu image here

</details>

<details><summary>Category Choice</summary>

Add category choice image here

</details>

<details><summary>Difficulty Choice</summary>

Add difficulty choice image here

</details>

<details><summary>Future Features</summary>  

- Ability for player to input their own words or categories that will be pushed to the google sheet.  
- Ability for the player to guess the whole word at once rather than letter by letter.
- Implementation of timed game mode that will allocate a specified amount to time to make a guess depending on the difficulty level.

</details>

## **Testing**  

### Python Linter Validation

Insert linter image here

### User Input Testing

| Test Area | Input To Validate | Expected Outcome | Actual Outcome | Pass/Fail |
| --------- | ----------------- | ---------------- | -------------- | --------- |
| Main Menu | N/A | Load main_menu function | As required | Pass |
| Main Menu | Input 0 | Quit the application | As required | Pass |
| Main Menu | Input 3 | Display credits | As required | Pass |
| Main Menu | Input 2 | Display rules | As required | Pass |
| Main Menu | Input 1 | Run the main game function | As required | Pass |
| Main Menu | Input any other number | Error message - Invalid choice - loop back to request input | As required | Pass |
| Main Menu | Input any other character | Error message - Not a number - loop back to request input | As required | Pass |
| Credits | Input 1 | Return to main menu | As required | Pass |
| Credits | Input 0 | Quit the application | As required | Pass |
| Credits | Input any other number | Error message - Invalid choice - loop back to request input | As required | Pass |
| Credits | Input any other character | Error message - Not a number - loop back to request input | As required | Pass |
| Rules | Input 1 | Return to main menu | As required | Pass |
| Rules | Input 0 | Quit the application | As required | Pass |
| Rules | Input any other number | Error message - Invalid choice - loop back to request input | As required | Pass |
| Rules | Input any other character | Error message - Not a number - loop back to request input | As required | Pass |
| Category Choice | Input 1 | Selects "Animals" category | As required | Pass |
| Category Choice | Input 2 | Selects "Brands" category | As required | Pass |
| Category Choice | Input 3 | Selects "Countries" category | As required | Pass |
| Category Choice | Input any other number | Error message - Invalid choice - loop back to request input | As required | Pass |
| Category Choice | Input any other character | Error message - Not a number - loop back to request input | As required | Pass |
| Difficulty Choice | Input 1 | Selects "Easy" difficulty | As required | Pass |
| Difficulty Choice | Input 2 | Selects "Intermediate" difficulty | As required | Pass |
| Difficulty Choice | Input 3 | Selects "Hard" difficulty | As required | Pass |
| Difficulty Choice | Input any other number | Error message - Invalid choice - loop back to request input | As required | Pass |
| Difficulty Choice | Input any other character | Error message - Not a number - loop back to request input | As required | Pass |
| Main Game Screen | Input a number | Error message - Invalid choice - loop back to request input | As required | Pass |
| Main Game Screen | Input multiple letters | Error message - One letter at a time - loop back to request input | As required | Pass |
| Main Game Screen | Correct letter guess | Display correct letter message, add letter to guessed letters list and display correctly guessed letter in the random word | As required | Pass |
| Main Game Screen | Guess all letters correctly | Display win message, display sub_menu to return to main menu or quit the application | As required | Pass |
| Main Game Screen | Incorrect letter guess | Display incorrect letter message, add letter to guessed letters list, remove one from guesses remaining and add body part to hangman | As required | Pass |
| Main Game Screen | Make 7 incorrect guesses | Display lose message, display sub_menu to return to main menu or quit the application | As required | Pass |

### Browser Tests

Insert table with images of app running on multiple browsers.

| Browser | Image | Result |
| ------- | ----- | ------ |
| Chrome | Insert image here | Working as expected |
| Firefox | Insert image here | Working as expected |
| Microsoft Edge | Insert image here | Working as expected |

### Bugs and Errors

No bugs were found in the program and everything is working as expected.

## **Technology Used**  

- Python programming language
- Github
- Gitpod
- Google sheets
- Google cloud
- Balsamiq
- Lucidchart 
  
### Imports

- random - Allow a random word to be chosen.
- os - Allow clear function to clear terminal.
- gspread - Allow program to link with google sheets.
- colorama - Allow terminal print messages to be colored.

## **Deployment**  

## **Credits**  

<details><summary>Media</summary>  

Add ascii links here
Flowchart made using lucidchart
Wireframes made using Balsamiq

</details>  

<details><summary>Code</summary>  

- Colorama tutorial
- Code institute tutors
- Fellow students in the CI Slack community
- Stack overflow
- Mentor Chris Quinn

</details>  