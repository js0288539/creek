# Python Crash Course 2e
# Exercise 10.8

def cats_dogs():
    filenames = ['cats.txt', 'dogs.txt']

    for filename in filenames:
        try:
            with open(filename) as f:
                contents = f.readlines()
            for l in contents:
                print(l.strip())
        except FileNotFoundError:
            print(f"Error: {filename} not found.")

# Exercise 10.9

def cats_dogs_silent():
    filenames = ['cats.txt', 'dogs.txt']

    for filename in filenames:
        try:
            with open(filename) as f:
                contents = f.readlines()
            for l in contents:
                print(l.strip())
        except FileNotFoundError:
            pass
            
