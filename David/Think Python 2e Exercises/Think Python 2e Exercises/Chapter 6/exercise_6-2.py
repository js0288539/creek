# Think Python 2e
# Exercise 6.2

def ack(m,n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    else:
        return ack(m - 1, ack(m, n - 1))

# larger values of m and n result in a RecursionError where the
# number of recursive calls exceeds the maximum recursion depth.
