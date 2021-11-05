'''
Problem:
    Finding a Linux commands from the input. All the commands are saved in .txt files and AI (thefuzz) decides what
    3 commands are best bets.
Authors:
    Adam Tomporowski, s16740
    Piotr Baczkowski, s16621
'''

# To run this program you need to install and import below modules in same format
from thefuzz import process

with open("commands.txt", "r") as f:
    commands = f.read().split("\n")


def get_matches(query, choices, limit=3):
    """
    This function decides which (and how much) strings should be displayed.

    :param query: tells the program what we are looking for
    :param choices: tells the program in which data set we are searching
    :param limit: tells the program how much best bets we want
    :return: Returns best matching (to query) strings from choices param.
    """
    results = process.extract(query, choices, limit=limit)
    return results


while True:
    command = input("Insert command you are looking for: ")
    if command == "q" or command == "quit":
        break
    elif len(command.split()) > 1:
        with open("details.txt", "r") as f2:
            details = f2.read().split("\n")
            matches = get_matches(command, details)
        print((get_matches(command, details)))
    else:
        print(get_matches(command, commands))