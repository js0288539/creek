# Think Python 2e
# Exercise 6.4

# "A number, a, is a power of b if:
#       it is divisible by b AND
#       a/b is a power of b"

def is_power(a, b):
    if a == 1:
        return True
    else:
        if a%b != 0:
            return False
        else:
            return is_power((a/b), b)

# NOTE TO SELF:
# IF YOUR RECURSIVE CODE DOESN'T RETURN THE VALUES YOU WANT IT TO
# CHECK TO SEE IF YOU FORGOT A DAMNED RETURN STATEMENT.
