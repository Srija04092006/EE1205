import numpy as np
import matplotlib.pyplot as plt

# Read data from the text file
with open("data.txt", "r") as file:
    data = [line.strip().split() for line in file]

# Separate values of n and x(n)
n_values, x_values = zip(*[(int(line[0]), float(line[1])) for line in data])

# Plot the stem graph without grid
plt.stem(n_values, x_values, basefmt='b-', linefmt='r-', markerfmt='ro')
plt.title('')
plt.xlabel('n')
plt.ylabel('x_1(n)')
plt.grid(False)  # Remove the grid
plt.savefig('plot.png', dpi = 300, bbox_inches = 'tight')
