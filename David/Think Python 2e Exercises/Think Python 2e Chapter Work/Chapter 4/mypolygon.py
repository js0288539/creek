import math
import turtle
bob = turtle.Turtle()
print(bob)

for i in range(4):
    print("Hello!")

#1.

def square(t, length):
    for i in range (4):
        bob.fd(length)
        bob.lt(90)

# square (t, length): uses a for loop that executes 4 times to create a
#                       square with side length = length.

def polygon (t, length, n):
    for i in range (n):
        bob.fd(length)
        bob.lt((360/n))

# polygon (t, length, n):
#   draws a polygon. t is the turtle object that is used
#   for drawing. length is the length of the side
#   being drawn, and for the turning angle, the
#   formula that determines the interior angle of an
#   n-sided regular polygon, n / 360, is used. n is also used to dictate
#   how many times the loop is to be exectuted. This way, if n = 6, then
#   the loop will run 6 times, sides of length = length will be drawn,
#   and the drawing turtle will turn 60 degrees.

def circle (t, r):
    polygon(bob, (2 * math.pi), r)

def circle_two (t, r):
    arc(t, r, 360)

# circle (t, r):
#   draws a circle. t is the turtle object that is used for drawing,
#   and r is the radius of the circle to be drawn. the function call to
#   polygon draws a polygon of a length of 2pi, with r being the turning
#   angle and # of times the loop executes. This follows the formula of
#   2(pi)r = circumfrence.

def arc (t, r, angle):
    length = (2 * math.pi * angle / 360)
    degrees = (angle/r)
    for i in range (r):
        bob.fd(length)
        bob.lt(degrees)


# hypothetical circle generalization:
# def circle (t, r):
#   arc(t, r, 360)

arc(bob, 100, 90)

turtle.mainloop()
