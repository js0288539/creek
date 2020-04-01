# Python Crash Course 2e
# Exercise 10.3, 10.4, 10.5

# guests.py

# username = input("Hello! Please enter your name: \n")

# with open("guest.txt", 'w') as file_object:
#    file_object.write(username)

def guest_book():

    exitcond = "steely"

    while exitcond != "0":
        
        username = input("Hello! Please enter your name, or enter 0 to exit: \n")
        
        print(f"Greetings, {username}! Your activity has been recorded.\n")

        with open("guest_book.txt", 'a') as file_object:
            file_object.write(f"{username} has visited.\n")

        exitcond = input("Please enter 1 to begin again or 0 to exit.")

def why_prog():
    exitcond = "steely"

    while exitcond != "0":

        reason = input("Why do you like programming? \n")
        with open("questionnaire.txt", 'a') as file_object:
            file_object.write(reason)

        print("Thank you for your input. Enter 1 to begin again or 0 to close.\n")
        exitcond = input()
