# Python Crash Course 2e
# Project 2
# Exercises 15.1 and 15.2:

import matplotlib.pyplot as plt

x_values = range(1,5001)
y_values = [x**3 for x in x_values]

# Plot setup:
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.copper, s = 10)

# Chart titles + labels:
ax.set_title("Cubic Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Cube of Value", fontsize = 14)

# Size of tick label:
ax.tick_params(axis = 'both', labelsize = 14)

plt.show()
