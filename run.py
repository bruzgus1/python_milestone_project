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

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('anime_watchlist')

watchlist_col = SHEET.worksheet("watchlist").col_values(1)

watchlist_col.pop(0)

print(watchlist_col)

print()

user_input = input("Anime Title you wish to add to the list: ")


def check_user_entry():

    """
    Checks if the Anime Title the user entered already exists in the worksheet
    """
    if user_input in watchlist_col:
        row_index = watchlist_col.index(user_input)+2
        print()
        question = input("Entry already exist, have you seen this Anime?, Please answer yes/no: ")
        if question == "yes":
            SHEET.worksheet("watchlist").update(f"B{row_index}", "yes")
        elif question == "no":
            SHEET.worksheet("watchlist").update(f"B{row_index}", "no")
        else:
            print("Wrong user input, Quiting program...")
    else:
        col_index = len(watchlist_col)+2
        question = input("Have you seen this Anime?, Please answer yes/no: ")
        SHEET.worksheet("watchlist").update(f"A{col_index}", user_input)
        if question == "yes":
            SHEET.worksheet("watchlist").update(f"B{col_index}", "yes")
        elif question == "no":
            SHEET.worksheet("watchlist").update(f"B{col_index}", "no")
        else:
            print("Wrong user input, Quiting program...")


check_user_entry()
