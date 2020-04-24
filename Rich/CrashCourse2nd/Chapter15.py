# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 10:20:54 2020
https://stackoverflow.com/questions/39241912/matplotlib-plt-show-method-does-not-pop-out-the-window
In Spyder, click Tools, Preferences, Ipython Console, Graphics. Under Graphics, change Backend to “automatic” instead of “inline”.

son of a bitch :-(   

@author: owner
"""

#%%
## IMPORT
import matplotlib.pyplot as plt


#%%
## CLASS

#%%
## FUNCTIONS

#%%
## DEFINES

input_values = range(1,6,1)
squares = [x**2 for x in input_values]

#%% MAIN


#%% EXAMPLE 01
fig1, ax1 = plt.subplots()
ax1.plot(squares)

plt.show()

#%% EXAMPLE 02
fig2, ax2 = plt.subplots()
ax2.plot(squares,linewidth=3)
ax2.set_title("Square Numbers",fontsize=24)
ax2.set_xlabel("Value",fontsize=14)
ax2.set_ylabel("Square of Value",fontsize=14)
ax2.tick_params(axis='both',labelsize=14)

plt.show()

#%% EXAMPLE 03

fig3, ax3 = plt.subplots()

ax3.plot(input_values,squares,linewidth=3)

plt.show()

#%% EXAMPLE 04
"""
   plt.style.available # in the console tells you what plot types are available
"""

plt.style.use('seaborn')
fig4, ax4 = plt.subplots()

ax4.plot(input_values,squares,linewidth=3)

plt.show()

#%% EXAMPLE 05
x_values = range(1,6,1)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values,y_values,s=100)



#%%
## EXAMPLE 06 - RESTART KERNAL
import matplotlib.pyplot as plt

x_values = range(1,1001)
y_values = [x**2 for x in x_values]
save_file = 'squares'

plt.style.use("seaborn")
fig, ax = plt.subplots()
# ax.scatter(x_values,y_values,s=10)
# ax.scatter(x_values,y_values,c='red',s=10) # named color
# ax.scatter(x_values,y_values,c=(0,0.8,0),s=10) # RGB Color
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=10) # Assign Y values to a color map

# set chart title and lable axis
ax.set_title("Square Numbers",fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Square of Value",fontsize=14)
ax.tick_params(axis='both',labelsize=14)

# set the range
ax.axis([0,1100,0,1100000])

plt.show()

#%%
## EXAMPLE 07 - RESTART THE KERNAL

from random import choice
import matplotlib.pyplot as plt

#

class RandomWalk:
    """ A class to generate random walks"""
    def __init__(self,num_points=5000):
        """ Initialize attributes of a randome walk, default is 5000 """
        self.num_points = num_points
        
        # All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]
        
    def fill_walk(self):
        """ Calculate all the points in the walk """
        # Keep talking steps until the walk reaches num_points
        while(len(self.x_values) < self.num_points):
            # Decide which direction to go and how far
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance
            
            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance
            
            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue
            
            # calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            
            self.x_values.append(x)
            self.y_values.append(y)

#
# Make a random walk
# while True:
# Make several random walks
rw = RandomWalk()

rw.fill_walk()

# Plot the points in the walk
plt.style.use('classic')
fig,ax = plt.subplots()              
ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
#    keep_running = input("Make another walk? (y/n) :")
#    if keep_running == 'n':
#        break
    
print('Done')
