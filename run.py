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

watchlist = SHEET.worksheet("watchlist").col_values(1)

watchlist.pop(0)

print(watchlist)

user_input = input("Anime Title you wish to add to the list: ")


def check_user_entry():

    """
    Checks if the Anime Title the user entered already exists in the worksheet
    """
    for i in watchlist:
        if i == user_input:
            print("Error entry already exist")


check_user_entry()
