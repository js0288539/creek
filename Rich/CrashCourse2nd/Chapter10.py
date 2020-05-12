# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 20:06:27 2020

@author: owner
"""

#%% Chapter 10
## IMPORT

#%%
## CLASSES

#%%
## FUCNTIONS

#%%
## DEFINES

fn_pidigits = r'LocLib/chapter_10/pi_digits.txt'

fn_output = r'LocLib/chapter_10/output.txt'
fn_output2 = r'LocLib/chapter_10/guest.txt'


#%% MAIN 01

with open(fn_pidigits) as fileo:
    contents = fileo.read()
    
print(contents)
fileo.close()

#%% MAIN 02
with open(fn_pidigits) as fileo:
    for line in fileo:
        print(line.rstrip())
        
fileo.close()
        
#%% MAIN 03

with open(fn_output,'w') as fileo:
    fileo.write('I love programming.\n')
    fileo.write('Die, oxygen breather!\n')

fileo.close()

with open(fn_output,'a') as fileo:
    fileo.write('PUT DOWN THAT GUN!\n')
    fileo.write('ZAAAAAAPPPPP!\n')
    
#%% MAIN 04

res = input('Please enter your full name > ')
res = res + '\n'

with open(fn_output2,'w') as fileo:
    fileo.write(res)
    
fileo.close()
