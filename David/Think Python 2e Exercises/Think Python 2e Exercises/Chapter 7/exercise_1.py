# 7.9 - Exercise 1
# Copy the loop from Section 7.5 and encapsulate it in a function called
# mysqrt that takes "a" as a parameter, chooses a reasonable value of
# x, and returns an estimate of the square root of a.

# Newton's method = y = ((x + a/x) / 2)
# a = number to have square root found
# x = any estimate number
# y = the actual square root of a

import math

def mysqrt(a):
    x = (a/2)
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < 0.0000001:
            print(x)
            break
        x = y

# A better, sexier square root loop function that actually has a return value

def mysquareroot(a):
    x = (a/2)
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < 0.0000001:
            return x
        x = y

# table requirements
# column 1 -> [3] -> mysqrt(a) -> [10]

def test_square_root():
    
    print("a" + (" " * 3) + "mysqrt(a)" + (" " * 10) + "math.sqrt(a)" + (" " * 7) + "diff")
    print("-" + (" " * 3) + "--------" + (" " * 11) + "-----------" + (" " * 8) + "----")
    for i in range(1, 10):
        sqrt_str_1 = str(mysquareroot(i))
        sqrt_str_2 = str(math.sqrt(i))
        sqrt_diff = abs(mysquareroot(i) - math.sqrt(i))
        diff_str = str(sqrt_diff)
        print(str (i) + (" " * 3) + sqrt_str_1 + ((19 - len(sqrt_str_1)) * " ") + sqrt_str_2 + ((19 - len(sqrt_str_2)) * " ") + diff_str)
