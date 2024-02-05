import numpy as np
import matplotlib.pyplot as plt

def sequence_x(n):
    return n**2 / 2**n

# Generate values for n from 0 to 10
n_values = np.arange(0, 11)
x_values = [sequence_x(n) for n in n_values]

# Plotting the sequence using a stem plot
plt.stem(n_values, x_values, use_line_collection=True, label='x(n)')  # use_line_collection for performance
plt.title('Stem plot of $x(n) = \\frac{n^2}{2^n}$')
plt.xlabel('n ')
plt.ylabel('$x(n)$')
plt.grid(True)
plt.xticks(n_values)  

# Highlight x(6)
highlight_n = 6
highlight_x = sequence_x(highlight_n)
plt.stem([highlight_n], [highlight_x], 'r', markerfmt='ro', basefmt=" ", linefmt='r', label='x(6) ')

plt.legend()
plt.show()

