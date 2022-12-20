# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
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

easy_animal_words = SHEET.worksheet("easy_animals").get_all_values()
intermediate_animal_words = SHEET.worksheet("intermediate_animals").get_all_values()
hard_animal_words = SHEET.worksheet("hard_animals").get_all_values()

easy_brand_words = SHEET.worksheet("easy_brands").get_all_values()
intermediate_brand_words = SHEET.worksheet("intermediate_brands").get_all_values()
hard_brand_words = SHEET.worksheet("hard_brands").get_all_values()

easy_country_words = SHEET.worksheet("easy_countries").get_all_values()
intermediate_country_words = SHEET.worksheet("intermediate_countries").get_all_values()
hard_country_words = SHEET.worksheet("hard_countries").get_all_values()


def main_menu():
    print(r"""\
                                                               
 | | | |   __ _   _ __     __ _   _ __ ___     __ _   _ __  
 | |_| |  / _` | | '_ \   / _` | | '_ ` _ \   / _` | | '_ \ 
 |  _  | | (_| | | | | | | (_| | | | | | | | | (_| | | | | |
 |_| |_|  \__,_| |_| |_|  \__, | |_| |_| |_|  \__,_| |_| |_|
                          |___/                            
    """)
    print(r"""\
             |\|
             |\|
             |\|
             |\|
             |\|
             |\|
             |_| 
            (___)
            (___)
            (___)
            (___)
            (___)
            (___)
          ,(/   \),
         ('/     \')
        ('/       \')
        |/|       |/|
        |/|       |/|
        |/|       |/|
        (-\       /-)
         \-\     /-/
          \-\___/-/ 
           '-----'
    """)
    print("[1] Play Game")
    print("[2] Rules")
    print("[3] Credits")
    print("[0] Quit")
    
main_menu()
