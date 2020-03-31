# Think Python 2e
# Exercise 5.5.

import math
import turtle
bob = turtle.Turtle()

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

draw(bob, 15, 5)

# draw is a function that takes 3 parameters:
#   t = the turtle object
#   length = length of the base line segment in pixels
#   n = base number of iterations

# this function draws trees!

# i get how it works, i just think that drawing out a state diagram
# for this will take hours, considering how many recursive calls
# this program actually makes during execution
