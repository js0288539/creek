# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 18:46:29 2020

@author: owner
"""

#%% IMPORT
import math


#%% DEFINE

def estimate_pi(tolerance):
    # pass in the tolerance [t] for the estimate
    f1 = (2.0 * math.sqrt(2.0))/9801.0 # first factor in the Srinivasa Ramanujan infinite series
    result = 0 # first result
    k=0
    sigres0 = 0
    sigres1 = 0
    
    while(sigres1 > tolerance):
        
        numerator = (math.factorial(4*k)*(1103 + 26390*k))
        denominator = (math.factorial(k)**4 * 396**(4*k))
        sigres1 = numerator / denominator
        result = f1 * (sigres0 + sigres1)
        sigres0 = sigres0 + sigres1
        k = k + 1
    return result
        


#%% VARIABLES AND CONSTANTS

inv_pi = 1 / math.pi
tolerance = 1e-15


#%% EXERCISE 7.3
print("Starting")
res = estimate_pi(tolerance)
print (res)



