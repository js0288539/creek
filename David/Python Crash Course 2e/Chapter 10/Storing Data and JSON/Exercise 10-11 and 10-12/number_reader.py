# Python Crash Course 2e
# Exercise 10.11
# number_writer.py

import json

filename = "number.json"

number = input("What's your favorite number?\n")

with open(filename, 'w') as f:
    json.dump(number, f)
    print("Your number has been saved!")
