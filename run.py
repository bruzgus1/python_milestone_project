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


def main():

    """ Activates everything inside the program """

    global WATCHLIST_COL

    WATCHLIST_COL = SHEET.worksheet("watchlist").col_values(1)  # access all the titles in the spreadsheet

    WATCHLIST_COL.pop(0)  # removes the first item in the list that is not needed for the program

    print(WATCHLIST_COL)  # temporary to see what kind of list I have now

    print()
    print("-----------------------------------------------------------------------------------")
    print("Welcome, this program was created to help you keep track")
    print("of the anime titles you have already seen")
    print("the program won't let you have duplicate names on your list")
    print("so you don't have to wonder if you have accidentally entered the same title twice")
    print("-----------------------------------------------------------------------------------")
    print()
    print("Program Starting...")
    print()

    global USER_INPUT

    USER_INPUT = input("Anime Title you wish to add to the list: ")

    if USER_INPUT == "":
        print()
        print("Wrong user input, Quiting program...")
    else:
        check_user_entry()


def check_user_entry():

    """
    Checks if the Anime Title the user entered already exists in the worksheet
    """
    if USER_INPUT in WATCHLIST_COL:
        print()
        print("scanning your list...")
        print()
        row_index = WATCHLIST_COL.index(USER_INPUT)+2
        question = input("Entry already exist, have you seen this Anime?, Please answer yes/no: ")
        print()
        if question == "yes":
            print("adding your inputs to google sheets...")
            SHEET.worksheet("watchlist").update(f"B{row_index}", "yes")
            print()
            print("inputs have been added...")
        elif question == "no":
            print("adding your inputs to google sheets...")
            SHEET.worksheet("watchlist").update(f"B{row_index}", "no")
            print()
            print("inputs have been added...")
        else:
            print()
            print("Wrong user input, Quiting program...")
    else:
        print()
        print("scanning your list...")
        print()
        col_index = len(WATCHLIST_COL)+2
        question = input("Have you seen this Anime?, Please answer yes/no: ")
        SHEET.worksheet("watchlist").update(f"A{col_index}", USER_INPUT)
        print()
        if question == "yes":
            print("adding your inputs to google sheets...")
            SHEET.worksheet("watchlist").update(f"B{col_index}", "yes")
            print()
            print("inputs have been added...")
        elif question == "no":
            print("adding your inputs to google sheets...")
            SHEET.worksheet("watchlist").update(f"B{col_index}", "no")
            print()
            print("inputs have been added...")
        else:
            print()
            print("Wrong user input, Quiting program...")


main()
