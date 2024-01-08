
import matplotlib.pyplot as plt
import numpy as np

# Define the function for the nth term
def a_n(n):
    return n**2 / 2**n

# Generate values for n
n_values = np.arange(0, 11)  # Adjust the range as needed

# Calculate corresponding values for a_n
a_n_values = [a_n(n) for n in n_values]

# Plot the graph
plt.plot(n_values, a_n_values, marker='o')
plt.title(r'Graph of $a_n = \frac{n^2}{2^n}$')
plt.xlabel('n')
plt.ylabel(r'$a_n$')
plt.grid(True)
plt.show()
