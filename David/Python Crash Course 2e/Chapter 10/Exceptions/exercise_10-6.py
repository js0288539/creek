# Python Crash Course 2e
# Exercise 10.6

def addition():
    print("Please enter two numbers to be added together:\n")
    x = input("First number: ")
    y = input("Second number: ")
    try:
        x = int(x)
        y = int(y)
        result = x + y
    except ValueError:
        print("One of those values isn't a number, you stupid shit.")
    else:
        print(result)

# Exercise 10.7

def addition_loop():
    while True:
        print("Please enter two numbers to be added together, ")
        print("or enter 'close' to exit.")
        
        x = input("\nFirst number: ")
        if x == "close":
            break
        y = input("Second number: ")
        if y == "close":
            break

        try:
            x = int(x)
            y = int(y)
            result = x + y
        except ValueError:
            print("Error: One of those values is not a number.")
        else:
            print(result)
            print("\n")
