# Exercise 10.7:
# Write a function called has_duplicates that takes a list and returns True
# if there is any element that appears more than once. It should NOT modify
# the original list.

def has_duplicates(t):
    t_copy = t
    t_copy.sort()
    for i in range(len(t_copy) - 1):
        if t_copy[i] == t_copy[i+1]:
            return True
    return False
