# If you are given three sticks, you may or may not be able to arrange
# them in a triangle. For any three lengths, there is a simple test to
# see if it is possible to form a triangle:

# If any of the three lengths is greater than the sum of the other two,
# then you cannot form a triangle.
# Otherwise, you can. (If the sum of two lengths equals the third, they
# form what is called a "degenerate triangle")

def is_triangle(x, y, z):
    if((x > (y+z)) or (y > (x+z)) or (z > (x+y))):
        print("No, this cannot form a triangle.")
    else:
        print("Yes, this can form a triangle.")

a = input("Please enter an integer value for x:\n")
a_int = int(a)

b = input("Please enter an integer value for y:\n")
b_int = int(b)

c = input("Please enter an integer value for z:\n")
c_int = int(c)

is_triangle(a_int, b_int, c_int)
