# Python Crash Course 2e
# Project 2
# Exercise 15.3
#   Modify rw_visual.py by replacing ax.scatter() with ax.plot(). To simulate
#   the path of a pollen grain on the surface of a drop of water, pass in
#   the rw.x_values and rw.y_values, and include a linewidth argument.
#   Use 5000 instead of 50,000 points.

# rw_visual_plot.py

import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # Make a random walk:
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk:
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize = (15,9))
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=3)

    # Remove the axes:
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
