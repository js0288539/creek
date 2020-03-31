#RECURSION IS YOUR WHITE WHALE
#YOU CAN DO THIS
#SLAY YOUR ENEMY

def countdown(n):
    if n<=0:
        print("Blast off!")
    else:
        print(n)
        countdown(n-1)


countdown(5)
