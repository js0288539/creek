# Exercise 13.1

# Write a program that reads a file, breaks each line into words, strips
# whitespace and punctuation from the words, and converts them to lowercase.

# HINT: The string module provides a string named whitespace, which contains
# space, tab, newline, etc., and punctuation which contains all punctuation
# characters.

# To import the string module, simply begin the program with: import string.
# string.whitespace = contains all whitespace characters
# string.punctuation = contains all punctuation characters

import string

def lowerlines():
    filefind = input('Please type the name and extension of the file you wish to use:\n')
    fin = open(filefind)
    for line in fin:
        word = line.strip()
        wordlist = list(word)
        for i in range(len(wordlist)):
            if wordlist[i] in string.whitespace or wordlist[i] in string.punctuation:
                del wordlist[i]
        #wordstring = ''
        #for i in range (len(wordlist)):
        #    wordstring = wordstring + wordlist[i]
        #wordstring = wordstring.lower()
