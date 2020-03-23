# Exercise 10.5
# Write a function called is_sorted that takes a list as a parameter and
# returns True if the list is sorted in ascending order and False
# otherwise. For example:

# >>> is_sorted([1,2,3])
# True
# >>> is_sorted(['b', 'a'])
# False

test_one = [1,2,2]
test_two = ['b', 'a']

def is_sorted(t):
    checklist = []
    for i in range(len(t)):
        checklist.append(t[i])
    checklist.sort()
    for i in range(len(t)):
        if t[i] != checklist[i]:
            return False
        return True
