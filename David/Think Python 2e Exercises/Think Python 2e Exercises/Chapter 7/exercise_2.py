# Exercise 7.2
# The built-in function eval takes a string and evaluates it using the Python
# interpreter. For example:

# >>> eval ('1 + 2 * 3')
# 7

# >>> import math
# >>> eval('math.sqrt(5)')
# 2.2360679774997898

# Write a function called eval_loop that iteratively prompts the user,
# takes the resulting input and evaluates it using eval, and prints
# the result.

import math

def eval_loop():
    print("Welcome to the Python Evaluator. Type 'done' to exit.")
    while True:
        print("Please enter an equation to evaluate: ")
        equation = input()
        if equation != 'done':
            print(str(eval(equation)))
        else:
            print("Thank you for using the Python Evaluator.")
            break

        
