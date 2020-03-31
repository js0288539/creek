# Python Crash Course 2e
# Exercise 9.4

class Restaurant:
    
    def __init__(self, r_n, c_t):
        """r_n = restaurant name, c_t = cuisine type"""

        self.r_n = r_n
        self.c_t = c_t
        self.number_served = 0

    def describe_r(self):
        print(f"{self.r_n} is a restaurant that serves {self.c_t}.")

    def open_r(self):
        print(f"{self.r_n} is now open!")

    def set_number_served(self, n):
        self.number_served = n

    def incr_number_served(self, n):
        self.number_served = self.number_served + n

class IceCreamStand(Restaurant):

    def __init__(self, r_n, c_t, flavors):
        super().__init__(r_n, c_t)
        self.flavors = ["vanilla", "chocolate"]

    def display_flavors(self):
        print(f"This ice cream stand sells ice cream in these flavors: {self.flavors}")


lyles = IceCreamStand("Lyle's Ice Cream Love Shack", "ice cream", ["vanilla", "chocolate"])
lyles.display_flavors()
