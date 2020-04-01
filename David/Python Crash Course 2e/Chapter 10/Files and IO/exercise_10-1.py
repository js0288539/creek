# Think Python 2e
# Exercise 10.1, 10.2

# Print the contents once in three different ways:
#   1. Reading the entire file
#   2. Looping over the file object
#   3. Storing the lines in a list and working with them outside the with block.

def entire_file():
    with open('learning_python.txt') as pthon:
        contents = pthon.read()
        print(contents.rstrip())

def loop_over_object():
    with open('learning_python.txt') as pthon:
        for line in pthon:
            print(line.rstrip())

def outside_with():
    with open('learning_python.txt') as pthon:
        contents = pthon.readlines()

    for line in contents:
        print(line.rstrip())

def replacements():
    with open('learning_python.txt') as pthon:
        contents = pthon.readlines()

    for line in contents:
        modline = line.replace('Python', 'C++')
        print(modline.rstrip())
