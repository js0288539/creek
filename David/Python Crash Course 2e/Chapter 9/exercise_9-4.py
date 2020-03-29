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


shadow_dennys = Restaurant("Shadow Denny's", "evil Grand Slams")
print(shadow_dennys.number_served)
shadow_dennys.set_number_served(100)
print(shadow_dennys.number_served)
shadow_dennys.incr_number_served(100)
print(shadow_dennys.number_served)
