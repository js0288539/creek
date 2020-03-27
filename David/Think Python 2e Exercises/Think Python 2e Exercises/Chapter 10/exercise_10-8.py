# Think Python 2e
# Exercise 10.8

import random

def birth_list(n):
    birthday_list = []

    for i in range(n):
        birthday = random.randint(1,365)
        birthday_list.append(birthday)

    birthday_list.sort()
    return birthday_list
        
def birth_traversal():
    l = birth_list(23)
    matches = 0
    total = 0
    
    for i in range(len(l) - 1):
        total += 1
        if l[i] == l[i+1]:
            matches += matches

    result = (matches, total)
    return result

# I'm not sure if I'm doing this correctly, but I have a function that
#   makes a list happen, and a function that checks for matches.

        
