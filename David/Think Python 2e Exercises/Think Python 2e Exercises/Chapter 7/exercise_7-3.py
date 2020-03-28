# Think Python 2e
# Exercise 7.3

import math
# math.factorial(x)
# math.pi
# math.sqrt()

def estimate_pi():

    # FENCEPOST: evaluate summation at k = 0 OUTSIDE of the while loop,
    #               set k = 1 so that the while loop begins at the right
    #               position.
    
    fac1 = (2 * math.sqrt(2)) / 9801
    k = 1
    n0 = (math.factorial(4*0)) * (1103 + (26390 * 0))
    print(n0)
    d0 = (math.factorial(0)) * (396**(0))
    print(d0)
    summation = (n0 / d0)

    return summation

    #while (summation >= 1e-15):
    #    numerator = ((math.factorial(4*k)) * (1103 + (26390 * k)))
    #    denominator = ((math.factorial(k))**4) * (396**(4*k))
    #    summation = (summation + (numerator / denominator))
    #    k += 1

    #result = fac1 * summation
    #return result
    
