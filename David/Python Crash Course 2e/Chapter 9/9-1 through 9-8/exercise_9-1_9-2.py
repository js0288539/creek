# Python Crash Course 2e
# Exercise 9.1 & 9.2

class Restaurant:
    
    def __init__(self, r_n, c_t):
        """r_n = restaurant name, c_t = cuisine type"""

        self.r_n = r_n
        self.c_t = c_t

    def describe_r(self):
        print(f"{self.r_n} is a restaurant that serves {self.c_t}.")

    def open_r(self):
        print(f"{self.r_n} is now open!")

# Exercise 9.1:
# chokeys = Restaurant("Uncle Chokey's Chicken Shack", "fried chicken")

# print(chokeys.r_n)
# print(chokeys.c_t)
# chokeys.describe_r()
# chokeys.open_r()

# Exercise 9.2

arnies = Restaurant("Arnie's Avacado Shack", "avocados and avocado accessories")
kat = Restaurant("Kat Patties", "burgers of suspicious origin")
ross = Restaurant("Ross's Ham Dungeon", "ham and nothing else")

arnies.describe_r()
kat.describe_r()
ross.describe_r()
