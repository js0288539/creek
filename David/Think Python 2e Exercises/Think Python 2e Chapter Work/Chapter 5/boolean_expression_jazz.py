def booltest (x, y):
    if x < y:
        print ("x is less than y")
    elif x > y:
        print ("x is greater than y")
    else:
        print ("x and y are equal")

def nestbool (x, y):
    if x == y:
        print("x and y are equal")
    else:
        if x < y:
            print ("x is less than y")
        else:
            print ("x is greater than y")

# nested conditionals become difficult to read very quickly.
# avoid them if possible, or simplify them as best you can.

nestbool (2, 4)
nestbool (4, 2)
nestbool (2, 2)
