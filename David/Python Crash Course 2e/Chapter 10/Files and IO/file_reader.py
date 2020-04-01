# Python Crash Course 2e
# file_reader.py

def whole_file():
    with open('pi_digits.txt') as file_object:
        contents = file_object.read()
        print(contents.rstrip())

def line_by_line():
    with open('pi_digits.txt') as file_object:
        for line in file_object:
            print(line.rstrip())

def file_lines():
    with open('pi_digits.txt') as file_object:
        lines = file_object.readlines()

    for line in lines:
        print(line.rstrip())
