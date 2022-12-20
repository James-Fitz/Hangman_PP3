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

print(easy_animal_words)
print(intermediate_animal_words)
print(hard_animal_words)

print(easy_brand_words)
print(intermediate_brand_words)
print(hard_brand_words)

print(easy_country_words)
print(intermediate_country_words)
print(hard_country_words)