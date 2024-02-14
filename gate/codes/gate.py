import numpy as np
import matplotlib.pyplot as plt

# Function to create a symmetric triangular pulse
def symmetric_triangular_pulse(omega, width):
    return np.where(np.logical_and(-width <= omega, omega <= width), 1 - np.abs(omega) / (width), 0)

# Values for omega
omega_values = np.linspace(-2, 2, 1000)

# Compute corresponding values for the symmetric triangular pulse
y_values = symmetric_triangular_pulse(omega_values, 2)

# Set the figure size
fig, ax = plt.subplots(figsize=(4, 3))  # Adjust the dimensions (width, height) as needed

# Plot the graph
ax.plot(omega_values, y_values)
ax.set_title('')
ax.set_xlabel(r'')
ax.set_ylabel(r'')
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)  # Darkened x=0 axis
ax.set_xticks([-2, 0, 2])
ax.set_xticklabels(['-2ω', '0', '2ω'])
ax.set_yticks([0, 1])
ax.set_yticklabels(['0', 'ω'])

# Insert arrows for x and y-axes
ax.arrow(2, 0, 0.5, 0, head_width=0.05, head_length=0.1, fc='black', ec='black')
ax.text(2.5, -0.1, r'$\omega$', fontsize=12)

ax.arrow(0, 1, 0, 0.2, head_width=0.05, head_length=0.1, fc='black', ec='black')
ax.text(0.3, 1.3, r'$F(\omega)$', fontsize=12)

ax.grid(False)

# Save the figure
plt.savefig('plot2.png', dpi=300, bbox_inches='tight')

