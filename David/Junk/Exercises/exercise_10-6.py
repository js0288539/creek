# Exercise 10.6:
# Two words are anagrams if you can rearrange the letters from one to spell
# the other. Write a function called is_anagram that takes two strings and
# returns True if they are anagrams.

def is_anagram(a, b):
    a_list = list(a)
    a_list.sort()
    b_list = list(b)
    b_list.sort()
    
    # Space removal

    while a_list[0] == ' ':
        del a_list[0]
    while b_list[0] == ' ':
        del b_list[0]

    # Length check

    if len(a_list) != len(b_list):
        return False

    # Character check

    for i in range(len(a_list)):
        if a_list[i] != b_list[i]:
            return False
    return True

