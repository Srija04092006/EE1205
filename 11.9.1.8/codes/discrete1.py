import numpy as np
import matplotlib.pyplot as plt

def sequence_x(n):
    return n**2 / 2**n

# Generate values for n from 1 to 10 to focus on natural numbers
n_values = np.arange(0, 11)
x_values = [sequence_x(n) for n in n_values]

# Plotting the sequence using a stem plot
plt.stem(n_values, x_values, use_line_collection=True)  # use_line_collection for performance
plt.xlabel('n')
plt.ylabel('$x(n)$')
plt.grid(True)
plt.xticks(n_values)  # Ensure x-axis ticks only show the natural numbers in the range
plt.title('Stem plot of $x(n) = \\frac{n^2}{2^n}$ ')
plt.show()

