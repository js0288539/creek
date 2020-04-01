# Think Python 2e
# write_message.py

filename = "programming.txt"

with open(filename, 'w') as file_object:
    file_object.write("I love programming!\n")

def add_stuff():
    with open(filename, 'a') as file_object:
        file_object.write("I also love creating browser apps!")
