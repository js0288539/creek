# Python Crash Course 2e
# Dog class

# dog.py

class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

#
#

dog_1 = Dog("Kyle",4)

print(f"My dog's name is {dog_1.name}, and he is {dog_1.age} years old.")

dog_1.sit()
dog_1.roll_over()
