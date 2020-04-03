# Python Crash Course 2e
# Exercise 10.13
# remember_me.py

# for exercise 10.13, adding in a bunch of dumb verification checks to
# the greet_user function just cluttered it up and made it unnecessarily
# convoluted, so i just made a new function that verified the username
# and used that as the check in greetings()

import json

def greet_user():
    """Greet the user by name."""
    filename = "username.json"

    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            print(f"We'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back, {username}!")

# REFACTORED:

def new_username():
    filename = "username.json"
    username = input("What is your name?\n")

    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"Your username has been saved, {username}!")

    return username

def get_username():
    filename = "username.json"

    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        print("File not found.")
    else:
        return username

def verify_user(username):
    response = 0
    while True:
        print(f"Are you sure this is your username? [{username}]")
        answer = input("\ny = YES\nn = NO\n")
        if answer == 'y' or answer == 'Y':
            response = True
            break
        elif answer == 'n' or answer == 'N':
            response = False
            break
        else:
            print("Invalid response.\n")
    return response
            

def greetings():
    username = get_username()
    verify = verify_user(username)
    if verify == True:
        print(f"Welcome back, {username}!")
    else:
        new_username()
        print(f"\nWe'll remember you when you come back!")

greetings()
