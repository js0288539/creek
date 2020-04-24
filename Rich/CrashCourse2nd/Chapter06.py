# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 18:30:49 2020

@author: owner
"""
#%% IMPORTS
import math

#%% FUNCTIONS
def distance(p1, p2):
    dx2 = (p2[0] - p1[0]) ** 2
    dy2 = (p2[1] - p1[1]) ** 2
    return math.sqrt(dx2+dy2)

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result
    

#%% SECTION 1
    
p1 = [12.0,13.0]
p2 = [-5.0, -7.0]

d = distance(p1,p2)
print(d)

#%% SECTION 2

print(factorial(1024))

#%% CHAPTER 7 EXERCISE 7.3