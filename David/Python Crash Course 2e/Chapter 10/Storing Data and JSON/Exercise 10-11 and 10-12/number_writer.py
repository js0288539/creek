# Python Crash Course 2e
# Exercise 10.11
# number_reader

import json

filename = "number.json"

with open(filename) as f:
    number = json.load(f)
    print(f"I know your favorite number! It's {number}!")
