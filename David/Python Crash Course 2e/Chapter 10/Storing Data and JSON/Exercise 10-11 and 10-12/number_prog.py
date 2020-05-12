# Python Crash Course 2e
# Exercise 10.12
# number_prog.py

import json

filename = "numb_prog.json"

try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("What's your favorite number?\n")
    with open(filename, 'w') as f:
        json.dump(number, f)
        print("Now I know your favorite number!")
else:
    print(f"I know your favorite number! It's {number}!")
