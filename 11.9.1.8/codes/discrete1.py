import numpy as np
import matplotlib.pyplot as plt

def sequence_x(n):
    return n**2 / 2**n

# Generate values for n from 0 to 10 (you can adjust this range)
n_values = np.arange(0, 11)
x_values = [sequence_x(n) for n in n_values]

# Plotting the sequence
plt.plot(n_values, x_values, marker='o', linestyle='-', color='b')
plt.title('Sequence $x(n) = \\frac{n^2}{2^n}$')
plt.xlabel('n')
plt.ylabel('$x(n)$')
plt.grid(True)
plt.show()

