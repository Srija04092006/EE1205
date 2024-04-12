import sympy as sp

# Define symbols
s, z = sp.symbols('s z')

# Given transfer function
Ha_BP_s = 2.544e-5 * s**4 / (s**8 + 0.1151*s**7 + 0.51*s**6 + 0.0435*s**5 + 0.0957*s**4 + 0.0054*s**3 + 0.0078*s**2 + 0.0022*s + 0.00024)

# Perform substitution
substitution = ((1 - z**-1) / (1 + z**-1))
substituted_expression = Ha_BP_s.subs(s, substitution)

# Simplify the expression
simplified_expression = sp.simplify(substituted_expression)

# Print the result
print("Expression in z:")
print(simplified_expression)


