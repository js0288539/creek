def draw_grid():
    horizontal = "+----+----+\n"
    vertical = "|    |    |\n"
    print(horizontal + (vertical * 4) + horizontal + (vertical * 4) + horizontal)

def draw_fourByFour():
    horizontal = "+----+----+----+----+"
    vertical = "|    |    |    |    |"
    print(horizontal)
    print (((vertical + "\n") * 3) + vertical)
    print(horizontal)
    print (((vertical + "\n") * 3) + vertical)
    print(horizontal)
    print (((vertical + "\n") * 3) + vertical)
    print(horizontal)
    print (((vertical + "\n") * 3) + vertical)
    print(horizontal)

draw_fourByFour()
