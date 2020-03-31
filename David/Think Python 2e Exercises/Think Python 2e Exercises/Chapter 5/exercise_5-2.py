def check_fermat (a, b, c, n):
    if ((n > 2) and ((a**n + b**n) == c**n)):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work...")

# Input strings for ease of running

w = input("Please enter a value for a:\n")
w_int = int(w)

x = input("Please enter a value for b:\n")
x_int = int(x)

y = input("Please enter a value for c:\n")
y_int = int(y)

z = input("Please enter a value for n:\n")
z_int = int(z)

check_fermat(w_int, x_int, y_int, z_int)
