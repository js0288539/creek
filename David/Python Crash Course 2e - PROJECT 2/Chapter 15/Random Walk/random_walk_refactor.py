# random_walk_refactor.py

# Class doesn't work, I have no idea why, it just doesn't
# Every time I run it with rw_visual_refactor.py, it returns
# errors that make absolutely no sense, mostly:
# AttributeError: 'RandomWalk' object has no attribute 'x_values'
# Which is kind of incredible considering that I can see the definition
# of self.x_values in line 22 without even having to scroll, but y'know...

# ¯\_(ツ)_/¯ 

from random import choice

class RandomWalk:

    def __init__(self, num_points = 5000):
        self.num_points = num_points

        # All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        direction = choice([1,-1])
        distance = choice([0,1,2,3,4])
        step = direction * distance

        return step

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
