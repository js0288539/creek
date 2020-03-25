# 8.3 Book Exercise
# As en exercise, write a function that takes a string as an argument and
# displays the letters backward, one per line.

def backwardstring (string):
    index = (len(string) - 1)
    while index != 0:
        letter = string[index]
        print(letter)
        index = index - 1
    print(string[0])
