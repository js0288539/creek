# Python Crash Course 2e
# car.py

class Car:

    def __init__ (self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if milage>=self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def incr_odometer(self,miles):
        self.odometer_reading += miles

new_car = Car("audi","a4",2019)
print(new_car.get_descriptive_name())
new_car.read_odometer()
