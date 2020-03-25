# Exercise 9.4

# Write a function named uses_only that takes a word and a string of letters,
# and only returns True if the word contains ONLY letters on that list.

x = 'hoe alfalfa'
y = 'acefhlo'

def uses_only(word, letters):
    word_list = list(word)
    while ' ' in word_list:
        word_list.remove(' ')
    for i in word_list:
        if i not in letters:
            return False
    return True
