# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 20:28:33 2020

@author: owner
"""
#%%
import math

#%%

def sVol(r):
    return (4*math.pi*r**3)/3

#%%
print(sVol(5))

#%%
x = 'monty'

x1 = len(x)
x2 = 60 - x1
off = " " * x2
print(off + x)

#%%

print('{0:>60}'.format(x))

#%%

t1 = '+' + ' -' * 4 
t2 = t1 + ' ' + t1 + ' +'

s1 = '|' + '  ' * 4
s2 = s1 + ' ' + s1 + ' |'

"""
print(t2)
print(s2)
print(s2)
print(s2)
print(s2)
print(t2)
print(s2)
print(s2)
print(s2)
print(s2)
print(t2)
"""
print(t2,s2,s2,s2,s2,t2,s2,s2,s2,s2,t2,sep='\n')

#%%

def cPrint(corner,top,side):
    t1 = corner + (' ' + top) * 4
    t2 = t1 + ' ' + t1 + ' ' + corner
    
    s1 = side + '  ' * 4
    s2 = s1 + ' ' + s1 + ' ' + side
    print(t2,s2,s2,s2,s2,t2,s2,s2,s2,s2,t2,sep='\n')
    
    
cPrint('o','-','|')

#%%
import turtle
bob = turtle.Turtle()

bob.color('red')
bob.pensize(1)

for i in range(4):
    bob.fd(100)
    bob.lt(90)

#%%

def countdown1(n):
    if(n>0):
        print(n)
        countdown(n-1)
    else:
        print('Blastoff!')

def countdown2(n):
    for i in range(n,0,-1):
        print(i)
    print('Blastoff!')


countdown2(5)

#%%

fruit = 'banana'

print(fruit[:])

#%%
wlist = []

sIn = r'ThinkPython/words.txt'
fIn = open(sIn)
# print((fIn.readline()).strip())
for line in fIn:
    wlist.append(line.strip())
fIn.close()

#%%

