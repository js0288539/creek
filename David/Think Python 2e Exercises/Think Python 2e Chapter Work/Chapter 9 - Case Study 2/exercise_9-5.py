# Exercise 9.5

# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters
# AT LEAST ONCE.

x = 'tacocat'
y = 'taco'

def uses_all(word, letters):
    letters_list = list(letters)
    word_list = list(word)
    while ' ' in word_list:
        word_list.remove(' ')

    for i in letters_list:
        if i not in word:
            return False

    for i in word_list:
        if i not in letters:
            return False

    return True

def uses_all_words(letters):
    letters_list = list(letters)
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        word_list = list(word)
