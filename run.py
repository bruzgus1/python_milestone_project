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

    # access all the titles in the spreadsheet
    WATCHLIST_COL = SHEET.worksheet("watchlist").col_values(1)

    # removes the first item in the list that is not needed for the program
    WATCHLIST_COL.pop(0)

    # calls the starter print messages, line 59
    starting_print()

    # prints the current watchlist, line 179
    current_watchlist()

    # calls the first user input, line 78
    first_user_input()


def check_user_entry():

    """
    Checks if the Anime Title the user entered already exists in the worksheet
    """

    WATCHLIST_COL = SHEET.worksheet("watchlist").col_values(1)

    WATCHLIST_COL.pop(0)

    if LOWER_INPUT in WATCHLIST_COL:
        print()
        print("scanning your list...")
        print()
        title_in_list()  # line 94
    else:
        print()
        print("scanning your list...")
        print()
        title_not_in_list()  # line 120


def starting_print():
    """
    prints the messages that the user is shown
    at the start of the program
    """

    print()
    print("---------------------------------------------------------------")
    print("Welcome, this program was created to help you keep track")
    print("of the anime titles you have already seen")
    print("the program won't let you have duplicate names on your list")
    print("so you don't have to wonder")
    print("if you have accidentally entered the same title twice")
    print("---------------------------------------------------------------")
    print()
    print("Program Starting...")
    print()


def first_user_input():
    """ executes the first user input """

    user_input = input("Anime Title you wish to add to/edit in the list: \n")

    global LOWER_INPUT

    LOWER_INPUT = user_input.lower()

    if LOWER_INPUT == "":
        print("Wrong user input, Try again...")
        print()
        first_user_input()
    else:
        check_user_entry()  # line 42


def title_in_list():
    """
    follows up with another question if the title
    is found inside the list
    """

    WATCHLIST_COL = SHEET.worksheet("watchlist").col_values(1)

    WATCHLIST_COL.pop(0)

    row_index = WATCHLIST_COL.index(LOWER_INPUT)+2
    question = input("Entry already exist, have you seen this Anime?\
    Please answer yes/no: \n")
    print()
    if question == "yes":
        print("adding your inputs to google sheets...")
        SHEET.worksheet("watchlist").update(f"B{row_index}", "yes")
        print()
        print("inputs have been added...")
        # asks if the user wants to add another title, line 152
        add_another_title()
    elif question == "no":
        print("adding your inputs to google sheets...")
        SHEET.worksheet("watchlist").update(f"B{row_index}", "no")
        print()
        print("inputs have been added...")
        # asks if the user wants to add another title, line 152
        add_another_title()
    else:
        print("Wrong user input, Try again...")
        print()
        title_in_list()


def title_not_in_list():
    """
    follows up with another question if the title
    is not found inside the list
    """

    WATCHLIST_COL = SHEET.worksheet("watchlist").col_values(1)

    WATCHLIST_COL.pop(0)

    col_index = len(WATCHLIST_COL)+2

    question = input("Have you seen this Anime?, Please answer yes/no: \n")
    print()
    if question == "yes":
        print("adding your inputs to google sheets...")
        SHEET.worksheet("watchlist").update(f"A{col_index}", LOWER_INPUT)
        SHEET.worksheet("watchlist").update(f"B{col_index}", "yes")
        print()
        print("inputs have been added...")
        # asks if the user wants to add another title, line 152
        add_another_title()
    elif question == "no":
        print("adding your inputs to google sheets...")
        SHEET.worksheet("watchlist").update(f"A{col_index}", LOWER_INPUT)
        SHEET.worksheet("watchlist").update(f"B{col_index}", "no")
        print()
        print("inputs have been added...")
        # asks if the user wants to add another title, line 152
        add_another_title()
    else:
        print("Wrong user input, Try again...")
        print()
        title_not_in_list()


def add_another_title():
    """ after adding the first title asks if you want to add another one """

    print()
    question = input("do you want to add/edit another title to/in the list?\
    Please answer, yes/no: \n")

    if question == "yes":
        print()
        first_user_input()
    elif question == "no":
        print()
        print("Understood, Program Shutting Down...")
    else:
        print()
        print("Wrong user input, Try again...")
        print()
        add_another_title()


def current_watchlist():
    """ Prints the current watchlist values """

    print("Current Watchlist:")

    answers = SHEET.worksheet("watchlist").col_values(2)

    answers.pop(0)

    i = 0
    number = 1
    while i < len(WATCHLIST_COL):
        print(f"{number}) {WATCHLIST_COL[i]}:{answers[i]}")
        i += 1
        number += 1
    print()


main()
