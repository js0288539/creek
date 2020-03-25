# Exercise 11.4:
# If you did Exercise 10.7, you already have a function named has_duplicates
# that takes a list as a parameter and returns True if there is any object
# that appears more than once in the list.

# Use a dictionary to write a faster, simpler version of has_duplicates.

# Original code:

# def has_duplicates(t):
#    t_copy = t
#    t_copy.sort()
#    for i in range(len(t_copy) - 1):
#        if t_copy[i] == t_copy[i+1]:
#            return True
#    return False

# Downey's solution:

def has_duplicates(t):
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False

# 1. An empty dictionary is created.
# 2. A for loop is initiated that traverses every element (x) of the list (t)
# 3. A conditional check is used to see if the given element (x) is in
#       the dictionary (d). If it IS, then it automatically returns True.
#       If it is NOT, then an entry is added to the dictionary, with the
#       key (x) being mapped to the value True.
# 4. If the loop finds another value in the list that matches up with the
#       key-value pairing in the dictionary, then it returns True. If not,
#       it returns False.
