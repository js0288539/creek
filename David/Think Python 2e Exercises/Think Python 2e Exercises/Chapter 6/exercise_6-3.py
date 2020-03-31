# Think Python 2e
# Exercise 6.3

# just pretend this is "palindrome.py"

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

# calling middle on a string with two letters returns an empty string.
# calling middle on a string with one letter returns an empty string.
# calling middle on an empty string returns an empty string.

def is_palindrome(s):
    if len(middle(s)) != 0:
        if first(s) == last(s):
            is_palindrome(middle(s))
        else:
            return False    
    return True
