# Exercise 9.2

# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.

# Modify your program from the previous section to print only the words that
# have no "e" and compute the percentage of the words in the list that
# have no "e".

def has_no_e(word):
    for char in word:
        if char == 'e':
            return False
    return True

def wordswithout_e():
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if 'e' not in word:
            print(word)

