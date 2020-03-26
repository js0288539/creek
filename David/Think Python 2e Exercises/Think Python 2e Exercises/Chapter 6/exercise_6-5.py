# Think Python 2e
# Exercise 6.5

# GCD of a and b is the LARGEST NUMBER  that divides both of them
#   with NO REMAINDER.
# For example, the GCD of 8 and 12 is 4.
#              the GCD of 62 and 36 is 2.

# One way to find them is based on the observation that if
#   r is the remainder when a/b, then
#   gcd(a, b) = gcd (b, r)

# base case is given: gcd(a,0) = a

def gcd (a, b):
    if a%b == 0:
        return b
    return gcd(b, a%b)

# i think this works, it returns the right value for each example above,
#   but i'm not sure what else to test it with.
