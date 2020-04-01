# Python Crash Course 2e
# pi_string.py

with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

pi_string = ""

for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
