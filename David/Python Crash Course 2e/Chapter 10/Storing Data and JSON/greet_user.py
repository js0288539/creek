# Python Crash Course 2e
# greet_user.py

import json

filename = "username.json"

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")
