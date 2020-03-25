# Think Python 2e
# Exercise 5.4.

def recurse (n, s):
"""Takes an integer s and adds n to it while recursing n times. n decreases
    by 1 every time the function recurses until it reaches 0."""

    if n == 0:
        print (s)
    else:
        recurse(n-1, n+s)

recurse(3, 0)

# recurse takes two numbers: n and s.
# base case is if n == 0, then s is printed normally.
# if n != 0, then the function is called again, subtracting 1
#   from the n value, and adding the current value of n to s.

# calling recurse(3,0) results in the following:

# recurse(3, 0) => n = 2, s = (0 + 3) = 3
# recurse(2, 3) => n = 1, s = (3 + 2) = 5
# recurse(1, 5) => n = 0, s = (5 + 1) = 6
# recurse(0, 6) => base case reached, print 6

#1. If recurse(-1, 0) was called, it would result in an infinite loop,
#   since the base case is not reached with its first call, and the
#   recursive calls can only decrement n by 1, so n = 0 will never be
#   reached.
