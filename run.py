import random
import os
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("hangman")


def clear():
    """
    Clears the console for the user.
    """
    os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')


def quit_game():
    """
    Quit the game and print a thank you message and ascii art to the console
    """
    clear()
    print("Thanks for playing...")
    print("""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░▄▄▀▀▀▀▀▄░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░▄▀░░░░░░░▀▄░░░░░░░░░░░░░░░░░░░░░░░░░░
░▄▀░░░▄▄░░░░▀▀▀▀▀▀▀▄▄▀▀▀▀▀▀▀▀▀▀▀▀▄▄░░░░
░█░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░▀▄░░
░█░░░░██▄████▄░██▄░░░░▄██░▄████▄░░░░▀▄░
░█░░░░██▀░░▀██▄░██▄░░██▀░██▀░▄██░░░░░█░
░█░░░░██░░░░███░░█████▀░░██▄█▀▀░░░░░░█░
░█░░░░███▄▄███▀░░░▀██▀░░░▀██▄▄▄██░░░░█░
░▀▄░░░░▀▀▀▀▀▀░░░░░██▀░░░░░░▀▀▀▀▀░░░░░█░
░░▀▄░░░░░░░░░░░░░██▀░░░▄▄░░░░░░░░░▄▄▀░░
░░░░▀▀▀▀▀▀▀▀▀▄░░░▀▀░░░▄▀░▀▀▀▀▀▀▀▀▀░░░░░
░░░░░░░░░░░░░▀▄░░░░░░▄▀░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░▀▀▀▀▀▀░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░""")
    exit()


def sub_menu():
    """
    Sub menu to be called containing main menu and quit options for user
    """
    print("[1] Main menu")
    print("[0] Quit")
    selection = int(input("Please select a number to continue...: \n"))
    if selection == 1:
        clear()
        main_menu()
    elif selection == 0:
        clear()
        quit_game()


def rules():
    print(
        """
        You will be given a choice of 3 categories to choose from.\n
        You will be given a choice of 3 difficulty levels to choose from.\n
        The object of the game is to guess to mystery word by guessing letters
        from the word.\n
        Each time you guess a letter incorrectly, another body part of the
        hangman will be drawn.\n
        When the hangman is complete, you lose.\n
        If you can guess the word before the hangman is complete, you win!\n
        """
    )
    sub_menu()


def credits_info():
    print(
        """
        This game was created by James Fitzpatrick for the Code Institute
        portfolio project 3.\n
        This game was created using the Python programming language.\n
        Github repository: https://github.com/James-Fitz\n
        LinkedIn: https://www.linkedin.com/in/james-fitzpatrick-6265b8248/\n
        Thank you to my mentor Chris Quinn for all of the fantastic advice
        throughout this project.\n
        """
        )
    sub_menu()


def main_menu():
    print(r"""
                     |/|
                     | |
                     |/|
                     | |
                     |/|
  _   _             (___)
 | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __
 | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
 |  _  | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    |___/

                    (___)
                    (___)
                    (___)
                    (___)
                    // \\
                   //   \\
                  ||     ||
                  ||     ||
                  ||     ||
                   \\___//
                    -----
                    """)
    print("[1] Play Game")
    print("[2] Rules")
    print("[3] Credits")
    print("[0] Quit")
    print("Welcome to Hangman!")
    selection = int(input("Please select a number to continue...: \n"))

    if selection == 1:
        clear()
        print("Starting game...")
        run_game()
        # clears the console and runs the main game
    elif selection == 2:
        clear()
        print("RULES")
        rules()
        # print rules for hangman to console
    elif selection == 3:
        clear()
        print("CREDITS")
        credits_info()
        # print thank you and credits to console
    elif selection == 0:
        quit_game()
    else:
        print(f"""{selection} is not a valid choice,
                please pick a number from the menu""")
        main_menu()
        # will print when an invalid selection is chosen


def category_choice():
    print("Please select a category...")
    print("[1] Animals")
    print("[2] Brands")
    print("[3] Countries")

    selection = int(input("Please select a number to continue...: \n"))

    if selection == 1:
        category = "animals"
    elif selection == 2:
        category = "brands"
    elif selection == 3:
        category = "countries"
    else:
        print("Invalid choice, try again")
        category_choice()
    clear()
    print(f"You selected { category.capitalize() }\n")
    return category


def difficulty_choice():
    print("Please select a difficulty level...")
    print("[1] Easy - 5 letter word")
    print("[2] Intermediate - 6 letter word")
    print("[3] Hard - 7 letter word")

    selection = int(input("Please select a number to continue...: \n"))

    if selection == 1:
        difficulty = "easy"
    elif selection == 2:
        difficulty = "intermediate"
    elif selection == 3:
        difficulty = "hard"
    else:
        print("Invalid choice, try again")
        difficulty_choice()
    clear()
    print(f"You selected { difficulty.capitalize() }\n")
    return difficulty


def run_game():
    category = category_choice()
    difficulty = difficulty_choice()
    new_game(category, difficulty)


def new_game(category, difficulty):
    """
    Starts a new game which takes the category and difficulty
    parameters chosen by the user to generate a word from the spreadsheet.
    """
    # Generate the word the player is trying to guess
    random_word = random.choice(SHEET.worksheet(difficulty + "_" + category).get_values().pop())
    # Print the category and difficulty level chosen by the user
    print(f"Category: { category.capitalize() }")
    print(f"Difficulty level: { difficulty.capitalize() }")
    print(f"your word is: {random_word}")
    print(len(random_word) * " _ ")

    guessed_letters = ""
    wrong_guesses = 0

    # Create a loop that ends when the player loses. Break if player wins
    while wrong_guesses < 6:
        player_choice = input("Please pick a letter...: \n")

        if player_choice in random_word:
            print(f"Correct, {player_choice} is in the word!")
        else:
            print(f"Sorry, {player_choice} is not in the word... You have {5 - wrong_guesses} guesses remaining")
            # Add 1 to the wrong_guesses variable
            wrong_guesses += 1
        # Adds all letters guessed by the user to the guessed_letters variable
        guessed_letters = guessed_letters + player_choice
        wrong_letters = 0

        for letter in random_word:
            if letter in guessed_letters:
                print(f"{letter}", end="")
            else:
                print(" _ ", end="")
                wrong_letters += 1

        if wrong_letters == 0:
            print(f"Congratulations, you won! The word is {random_word}!")
            sub_menu()
            break
        else:
            print("Sorry, you lose... Please try again...")
            sub_menu()


main_menu()
