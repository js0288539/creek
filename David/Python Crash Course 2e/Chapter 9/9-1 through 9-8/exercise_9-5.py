# Python Crash Course 2e
# Exercise 9.5

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

breen = User("Wallace","Breen",60,"M","Administrator","admin")
mossman = User("Judith","Mossman",55,"F","Theoretical Physics","staff")
freeman = User("Gordon","Freeman",27,"M","Theoretical Physics","n/a")

breen.describe_user()
breen.greet_user()
print("\n")
mossman.describe_user()
mossman.greet_user()
print("\n")
freeman.describe_user()
freeman.greet_user()
