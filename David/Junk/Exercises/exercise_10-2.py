# Exercise 10.2:
# Write a function called cumsum that takes a list of numbers and returns
# the cumulative sum; that is, a new list where the ith element is the sum
# of the first i + 1 elements from the original list. For example:

# >>> t = [1,2,3]
# >>> cumsum(t)
# [1,3,6]

t = [1,2,3]

def cumsum(t):
    sumlist = [t[0]]
    for i in range(len(t) - 1):
        x = sumlist[i]
        y = t[i + 1]
        sumlist.append(x+y)
    print(sumlist)
