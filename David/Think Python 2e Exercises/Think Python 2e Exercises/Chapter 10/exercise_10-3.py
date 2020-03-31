# Exercise 10.3:
# Write a function called middle that takes a list and returns a new list
# that contains all but the first and last elements. For example:

# >>> t = [1,2,3,4]
# >>> middle(t)
# [2,3]

t = [1,2,3,4]

def middle(t):
    midlist = []
    for i in range(len(t) - 2):
        midlist.append(t[i+1])
    return midlist

