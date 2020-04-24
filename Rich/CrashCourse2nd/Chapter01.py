# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 11:34:48 2020

@author: owner
"""
#%%
import math

#%%

print("Hello Python World")

#%% p73
fname = "ada"
lname = 'lovelace'

fullname = f"{fname} {lname}"
print(f"\t{fullname.title()}")

#%%
# point initialization as a tupble
p1 = 5.0,6.0

# the following causes an error because of the way the line above was defined
# p1[0] = 12

#
p2 = [10,12]
# this works because p2 is a list, not a tuple
p2[0] = 30

#%%

# lists are labels, not storage locations (WHY?!?!)
base = ['honda','yamaha','suzuki']
motorcycles = base[:]

print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles = base
motorcycles.insert(0,'ducati')
print(motorcycles)

#%%
for cycle in motorcycles:
    print(cycle)
    
#%%
r1 = list(range(1,10))
r2 = list(range(30,40))

r3 = r1 + r2

r4 = [ math.sqrt(v) for v in r3[5:15]]
print(r4)
