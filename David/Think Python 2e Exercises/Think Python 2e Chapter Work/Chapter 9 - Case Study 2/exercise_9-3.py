# Exercise 9.3:

# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any forbidden
# letters.

# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?

def avoids(word, letters):
    letter_list = list(letters)
    for i in range(len(letter_list)):
        if letter_list[i] in word:
            return False
    return True

def word_check():

    """A simple method used to quickly reference the number of words in words.txt"""
    
    fin = open('words.txt')
    counter = 0
    for line in fin:
        counter += 1
    print(str(counter))

def words_avoids():
    fin = open('words.txt')
    forbidden = input("Please enter forbidden letters: \n")
    forb_list = list(forbidden)
    counter = 0

    for line in fin:
        word = line.strip()
        checker = 0
        for i in range(len(forb_list)):
            if forb_list[i] not in word:
                checker += 1
        if checker == len(forb_list):
            counter += 1
    return counter
                
