# Exercise 10.1:
# Write a function called nested_sum that takes a list of integers and adds up
# the elements from all of the nested lists. For example:

# >>> t = [[1,2],[3],[4,5,6]]
# >>> nested_sum(t)
# 21

t = [[1,2],[3],[4,5,6]]

def nested_sum(nl):
    result = 0
    for i in range(len(nl)):
        element = nl[i]
        adding = sum(element)
        result = result + adding
    print(result)
