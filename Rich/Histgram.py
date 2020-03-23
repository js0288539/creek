# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 16:55:01 2020

@author: owner
"""


target_dir = "F:\Public\Documents\MANGA"
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
num_bins = 6
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
plt.show()
