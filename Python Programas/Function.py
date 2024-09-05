import matplotlib.pyplot as plt
import numpy as np

# Define the function parameters
a = 0.5
b = 0.5

# Define the x values
x = np.linspace(-10, 10, 400)

# Calculate acos(a*x + b) for all x values
# Ensure that the input to acos is within the domain [-1, 1]
# Clip values outside the domain to avoid errors
y = np.clip(a * x + b, -1, 1)
y = np.arccos(y)

# Plot the function
plt.plot(x, y, label='Acos(0.5 * x + 0.5)')

# Naming the x and y axes
plt.xlabel('x - axis')
plt.ylabel('y - axis')

# Giving a title to the graph
plt.title('Graph of Acos(0.5 * x + 0.5)')

# Adding a legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
