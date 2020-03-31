# Think Python 2e
# Exercise 6.1

def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c (x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

x = 1
y = x + 1
print(c(x, y+3, x+y))

# x = 1                         (x = 1)
# y = x + 1                     (y = 2)

# c(x, y + 3, x + y)            (x = 1, y = 5, z = 3)

#   total = 1 + 5 + 3           (total = 9)
#   square = b(total)**2

#       b(9):
#           prod = a(9, 9)

#               a(9, 9):
#                   x = x + 1   (x = 10)
#                   return x*y  (a(9,9) = 90)

#           print(z, prod)      (*print 9 90*)
#           return prod         (b(9) = 90)

#   // square = 90**2
#   return square               (square = 8100)
#
# 9 90
# 8100
