# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
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

easy_animals_words = SHEET.worksheet("easy_animals").get_all_values()
intermediate_animasl_words = SHEET.worksheet("intermediate_animals").get_all_values()
hard_animals_words = SHEET.worksheet("hard_animals").get_all_values()

easy_brands_words = SHEET.worksheet("easy_brands").get_all_values()
intermediate_brands_words = SHEET.worksheet("intermediate_brands").get_all_values()
hard_brands_words = SHEET.worksheet("hard_brands").get_all_values()

easy_countries_words = SHEET.worksheet("easy_countries").get_all_values()
intermediate_countries_words = SHEET.worksheet("intermediate_countries").get_all_values()
hard_countries_words = SHEET.worksheet("hard_countries").get_all_values()


"""
Clears the console for the user.
"""


def clear():
    # clears the screen for user
    os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')


def run_game():
    category = category_choice()
    difficulty = difficulty_choice()
    new_game(category, difficulty)
    

"""
Starts a new game which takes the category and difficulty
parameters chosen by the user to generate a word from the spreadsheet.
"""
def new_game(category, difficulty):
    random_word = random.choice(f"{difficulty}_{category}_words")
    print(category)
    print(difficulty)
    print(f"your word is: {random_word}")
    
    
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
            break
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

  
main_menu()