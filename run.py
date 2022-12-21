import gspread
import os 
import random

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


def rules():
    print(
        """
        You will be given a choice of 3 categories to choose from.\n
        You will be given a choice of 3 difficulty levels to choose from.\n
        The object of the game is to guess to mystery word by guessing letters from the word.\n
        Each time you guess a letter incorrectly, another body part of the hangman will be drawn.\n
        When the hangman is complete, you lose.
        If you can guess the word before the hangman is complete, you win!
        """"
    )
    print("[1] Main menu")
    print("[0] Quit")
    
    selection = int(input("Please select a number to continue...: \n"))
    if selection == 1:
        clear()
        main_menu()
    elif selection == 0:
        clear()
        print("Thanks for playing...")
        quit()
    else:
        print("Invalid choice, try again")
        rules()
    
    
    
def main_menu():

    print("[1] Play Game")
    print("[2] Rules")
    print("[3] Credits")
    print("[0] Quit")
    
    print("Welcome to Hangman!")
    selection = int(input("Please select a number to continue...: \n"))

    while selection != 0:
        if selection == 1:
            clear()
            print("Starting game...")
            run_game()
            break
            # clears the console and runs the main game
        elif selection == 2:
            print("Rules for hangman are as follows: (input rules here)")
            rules()
            
            # print rules for hangman to console
        elif selection == 3:
            print("Credits : thank you to ....")
            break
            # print thank yous and credits to console
        else:
            print("Invalid choice, try again")
            break
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
    random_word = random.choice(SHEET.worksheet(difficulty + "_" + category).get_values().pop())
    print(category)
    print(difficulty)
    print(f"your word is: {random_word}")
    

main_menu()

