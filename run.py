"""
Import all neccessary functions
"""
import random
import os
import gspread
import colorama
from google.oauth2.service_account import Credentials

colorama.init()

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
    print(colorama.Fore.CYAN + """
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
    Sub menu to be called containing main menu and quit options for user.
    """
    print(colorama.Fore.GREEN + "[1]" + colorama.Fore.WHITE + "Main menu")
    print(colorama.Fore.RED + "[0]" + colorama.Fore.WHITE + "Quit\n")
    while True:
        try:
            selection = int(input("Please select a number to continue...: \n"))
            if selection == 1:
                clear()
                main_menu()
            elif selection == 0:
                clear()
                quit_game()
            else:
                print(f"Error: {selection} is not an option...")
        except ValueError:
            print("Error: Not a number...")


def rules():
    """
    Print rules of game and run sub menu function.
    """
    print(colorama.Fore.YELLOW + "RULES".center(75))
    print(
        colorama.Fore.WHITE + """
        You will be given a choice of 3 categories to choose from.\n
        You will be given a choice of 3 difficulty levels to choose from.\n
        The object of the game is to guess to mystery word by guessing letters
        from the word, one at a time.\n
        Each time you guess a letter incorrectly, another body part of the
        hangman will be drawn.\n
        When the hangman is complete, you lose.\n
        If you can guess the word before the hangman is complete, you win!\n
        """
    )
    sub_menu()


def credits_info():
    """
    Print credits info and run sub menu function.
    """
    print(colorama.Fore.YELLOW + "CREDITS".center(75))
    print(
        colorama.Fore.WHITE + """
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
    """
    Print options for main menu to console.
    Run the appropriate function when user makes choice.
    """
    print(colorama.Fore.CYAN + r"""
  _   _
 | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __
 | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
 |  _  | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    |___/
                    """)
    print(colorama.Fore.WHITE + "Welcome to Hangman!\n".center(48))
    print(
        colorama.Fore.GREEN + "[1]".rjust(20, " ")
        + colorama.Fore.WHITE + " Play Game"
        )
    print(
        colorama.Fore.GREEN + "[2]".rjust(20, " ")
        + colorama.Fore.WHITE + " Rules"
        )
    print(
        colorama.Fore.GREEN + "[3]".rjust(20, " ")
        + colorama.Fore.WHITE + " Credits"
        )
    print(
        colorama.Fore.RED + "[0]".rjust(20, " ")
        + colorama.Fore.WHITE + " Quit\n"
        )
    while True:
        try:
            selection = int(input(
                colorama.Fore.WHITE +
                "Please select a number from the menu to continue...: \n"
                ))
            if selection == 1:
                clear()
                run_game()
                # clears the console and runs the main game
            elif selection == 2:
                clear()
                rules()
                # print rules for hangman to console
            elif selection == 3:
                clear()
                credits_info()
                # print thank you and credits to console
            elif selection == 0:
                quit_game()
            else:
                print(
                    colorama.Fore.RED +
                    f"Error: {selection} is not an option..."
                    )
        except ValueError:
            print(colorama.Fore.RED + "Error: Not a number...")


def category_choice():
    """
    Print categories for user to choose from.
    Return chosen category.
    """
    print("Please select a category...\n".center(48))
    print(
        colorama.Fore.GREEN + "[1]".rjust(15, " ")
        + colorama.Fore.WHITE + " Animals"
        )
    print(
        colorama.Fore.CYAN + "[2]".rjust(15, " ")
        + colorama.Fore.WHITE + " Brands"
        )
    print(
        colorama.Fore.YELLOW + "[3]".rjust(15, " ")
        + colorama.Fore.WHITE + " Countries"
        )
    while True:
        try:
            selection = int(input(
                colorama.Fore.WHITE +
                "Please select a number from the menu to continue...: \n"
                ))
            if selection == 1:
                category = "animals"
                return category
            elif selection == 2:
                category = "brands"
                return category
            elif selection == 3:
                category = "countries"
                return category
            else:
                print(
                    colorama.Fore.RED +
                    f"Error: {selection} is not an option..."
                    )
        except ValueError:
            print(colorama.Fore.RED + "Error: Not a number...")


def difficulty_choice():
    """
    Print difficulties for user to choose from.
    Return chosen difficulty.
    """
    print("Please select a difficulty level...\n".center(48))
    print(
        colorama.Fore.GREEN + "[1]".rjust(10, " ")
        + colorama.Fore.WHITE + " Easy:".ljust(15, " ")
        + " 5 letters"
        )
    print(
        colorama.Fore.YELLOW + "[2]".rjust(10, " ")
        + colorama.Fore.WHITE +
        " Intermediate:".ljust(15, " ") + " 6 letters"
        )
    print(
        colorama.Fore.RED + "[3]".rjust(10, " ")
        + colorama.Fore.WHITE +
        " Hard:".ljust(15, " ") + " 7 letters\n")
    while True:
        try:
            selection = int(input(
                "Please select a number from the menu to continue...: \n"
                ))
            if selection == 1:
                difficulty = "easy"
                return difficulty
            elif selection == 2:
                difficulty = "intermediate"
                return difficulty
            elif selection == 3:
                difficulty = "hard"
                return difficulty
            else:
                print(colorama.Fore.RED + f"Error: {selection} is not an option...")
        except ValueError:
            print(colorama.Fore.RED + "Error: Not a number...")


def print_hangman(wrong_guesses):
    """
    Takes the value of wrong guesses and prints the relevant hangman image
    """
    if wrong_guesses == 0:
        print(r"""
        ______
        |    |
        |
        |
        |
        |
        |________
        """)
    elif wrong_guesses == 1:
        print(r"""
        ______
        |    |
        |    O
        |
        |
        |
        |________
        """)
    elif wrong_guesses == 2:
        print(r"""
        ______
        |    |
        |    O
        |    |
        |
        |
        |________
        """)
    elif wrong_guesses == 3:
        print(r"""
        ______
        |    |
        |    O
        |    |/
        |
        |
        |________
        """)
    elif wrong_guesses == 4:
        print(r"""
        ______
        |    |
        |    O
        |   \|/
        |
        |
        |________
        """)
    elif wrong_guesses == 5:
        print(r"""
        ______
        |    |
        |    O
        |   \|/
        |    |
        |
        |________
        """)
    elif wrong_guesses == 6:
        print(r"""
        ______
        |    |
        |    O
        |   \|/
        |    |
        |     \
        |________
        """)
    elif wrong_guesses == 7:
        print(r"""
        ______
        |    |
        |    O
        |   \|/
        |    |
        |   / \
        |________
        """)
    else:
        quit()


def run_game():
    """
    Assign variables for category and difficulty.
    Use these variables to run new_game function.
    """
    category = category_choice()
    clear()
    difficulty = difficulty_choice()
    clear()
    new_game(category, difficulty)


def new_game(category, difficulty):
    """
    Starts a new game which takes the category and difficulty
    parameters chosen by the user to generate a word from the spreadsheet.
    """
    # Generate the word the player is trying to guess
    random_word = random.choice(
        SHEET.worksheet(difficulty + "_" + category)
        .get_values().pop())
    # Print the category and difficulty level chosen by the user
    print(f"Category: { category.capitalize() }")
    print(f"Difficulty level: { difficulty.capitalize() }")
    guessed_letters = ""
    wrong_guesses = 0
    print_hangman(wrong_guesses)
    print("your word is: ")
    print(len(random_word) * " _ ")
    # Create a loop that ends when the player loses. Break if player wins.
    while wrong_guesses < 7:
        player_choice = input("Please pick a letter...: \n").upper()
        print(f"Category: { category.capitalize() }")
        print(f"Difficulty level: { difficulty.capitalize() } \n")
        print_hangman(wrong_guesses)
        clear()
        if not player_choice.isalpha():
            print(
                f"{player_choice} is not a valid letter... \n"
                )
            print_hangman(wrong_guesses)
            print(
                f"\n Previously guessed letters: \n \
                { list(guessed_letters.upper()) }\n"
                )
        elif len(player_choice) != 1:
            print("Please input one letter at a time... \n")
            print_hangman(wrong_guesses)
            print(
                f"\n Previously guessed letters: \n \
                { list(guessed_letters.upper()) }\n"
                )
        elif player_choice in guessed_letters:
            print(f"{player_choice.upper()} has already been guessed...")
            print_hangman(wrong_guesses)
            print(
                f"\n Previously guessed letters: \n \
                    { list(guessed_letters.upper()) }\n"
                    )
        else:
            if player_choice in random_word:
                print(
                    f"Correct, {player_choice.upper()} is in the word! " +
                    f"You have {6 - wrong_guesses} guess(es) remaining...")
            else:
                print(
                    f"Sorry, {player_choice.upper()} is not in the word... " +
                    f"You have {6 - wrong_guesses} guess(es) remaining..."
                    )
                # Add 1 to the wrong_guesses variable
                wrong_guesses += 1
            print_hangman(wrong_guesses)
            # Adds all letters guessed by the user
            # to the guessed_letters variable.
            guessed_letters = guessed_letters + player_choice
            wrong_letters = 0
            for letter in random_word:
                if letter in guessed_letters:
                    print(colorama.Fore.GREEN + f" { letter.upper() } ", end="")
                else:
                    print(colorama.Fore.RED + " _ ", end="")
                    wrong_letters += 1
            print(f"\n Previously guessed letters: \n \
                { list(guessed_letters.upper()) }\n")
            if wrong_letters == 0:
                print(
                    f"\n Congratulations, you won! \
                    The word is {random_word.upper()}!\n")
                sub_menu()
                break
    else:
        print("\n Sorry, you lose... Please try again...\n")
        print(f"The word was {random_word.upper()}...\n")
        sub_menu()


main_menu()
