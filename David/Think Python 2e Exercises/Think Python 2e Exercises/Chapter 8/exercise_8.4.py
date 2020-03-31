# Think Python 2e
# Exercise 8.4

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

# any_lowercase1(s) does NOT work.
# the function begins with a for loop that iterates through every element
#   (c) of the parameter string (s). inside this for loop is a conditional
#   that checks to see if the current element is lowercase, but the way
#   it is set up means that it will ONLY check the first element before
#   returning either True or False, terminating the loop early and returning
#   an incorrect answer.

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

# any_lowercase2(s) does NOT work.
# the function begins with a for loop that works the same way as in the first
#   function, but the conditional checks to see if the individual character
#   'c' is lowercase, not the actual c variable that represents what
#   element of the string the loop is checking. Not only will this always
#   return True, but it won't even return the boolean, since it is
#   written that it returns a string ('True' and 'False').

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

# any_lowercse3(s) does NOT work.
# the function begins with a for loop that works the same way as in the first
#   function, but it sets a new variable, flag, equal to the boolean result
#   of c.islower(). the loop will iterate through every character as planned,
#   but once it reaches the final character in s, the loop terminates
#   and returns that result. the way the function is set up, it only
#   returns True or False based on whether or not the LAST character
#   in s is lowercase.

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

# any_lowercase4(s) WORKS.
# the function begins by setting a flag variable to False.
#   it then iterates through every character (c) in the string (s) with
#   a for loop, and for every iteration, it sets flag equal to
#   a conditional!
# flag or c.islower() will return False until it hits a lowercase letter,
#   whereupon the conditional will be made True, since c.islower() is True.
#   Since flag is now True, the or conditional will be True for
#   every single character afterward.
# In essence, the program assumes there is no lowercase letters with flag,
#   but when it hits a single lowercase letter, flag becomes true for every
#   character after that, since it is known that at least one lowercase letter
#   exists in the string. flag is then returned as True if a lowercase letter
#   is present.

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True

# any_lowercase5(s) does NOT work.
# the function begins with the same foor loop as before, but the conditional
#   checks to see if the character is NOT lowercase. if the function
#   detects any uppercase letters, the loop terminates and the function
#   returns False.

