# Think Python 2e
# Execrise 5.6.

import math
import turtle

bob = turtle.Turtle()


def koch(t, x):
    if x < 3:
        t.fd(x)
        return
    koch(t, x/3)
    t.lt(60)
    koch(t, x/3)
    t.rt(120)
    koch(t, x/3)
    t.lt(60)
    koch(t, x/3)


# the key to recursion is to follow instructions and don't think
#   about HOW the program works, just expect it to work
# if your program breaks, check to see if anything fundamental is broken
#   ( like forgetting a return statement -_- )
# if everything is _syntactically_ correct, rewrite it until it works
#   as intended, maybe rethink how you write the instruction set in the
#   first place

def snowflake(t, x):
    for i in range(3):
        koch(t, x)
        t.rt(120)
