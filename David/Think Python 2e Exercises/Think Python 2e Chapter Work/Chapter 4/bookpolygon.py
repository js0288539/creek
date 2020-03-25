# bookpolygon.py:
# demonstration of circle and arc methods as outlined by the book

import math
import turtle
bob = turtle.Turtle()
print(bob)

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circle(t, r):
    circumfrence = 2 * math.pi * r
    n = int(circumfrence / 3) + 3
    length = circumfrence / n
    polygon(t, n, length)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc (t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)

arc(bob, 100, 90)
