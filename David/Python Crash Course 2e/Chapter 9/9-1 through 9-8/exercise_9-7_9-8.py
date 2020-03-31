# Python Crash Course 2e
# Exercise 9.7 & 9.8

# PROBLEM:
# Whenever I initialize an instance of a class that has default values
#   defined in its init method, I can't actually initialize it properly
#   unless I put *something* in the initialization parameters. When I put
#   a dummy value in there, like 0, it works perfectly as intended, but
#   I have no idea if this causes any unintended behavior, and I also
#   have no idea if the book mentions this at all.

class User:

    def __init__(self, first_name, last_name, age, sex, occupation, clearance):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.occupation = occupation
        self.clearance = clearance
        self.login_attempts = 0

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Sex: {self.sex}")
        print(f"Occupation: {self.occupation}")

    def greet_user(self):
        if self.clearance == "admin":
            print(f"Welcome, administrator {self.last_name}.")
        elif self.clearance == "staff":
            print(f"Welcome, {self.first_name} {self.last_name}")
        else:
            print("Welcome, guest.")

    def incr_login_attempts(self):
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin:

    def __init__(self, privileges):
        self.privileges = Privileges(0)

class Privileges:

    def __init__(self, privileges):
        self.privileges = ["can add post", "can delete post", "can ban user"]
        
    def show_privileges(self):
        print(f"Admin privileges: {self.privileges}")

breen = Admin(0)
breen.privileges.show_privileges()
