import matplotlib.pyplot as plt
import numpy as np

#Acos(nwot0)
a = 3
# Define the x values
xs = -2 * np.pi # -2 * np.pi
xe =  2 * np.pi # 2 * np.pi
# Define vmax & vmin
vmax = 7
vmin = -4

x = np.linspace(xs, xe, 400)

# Calculate the y values (Acos(x))
y = a * np.cos(((vmax + vmin)/2)*x)

# Plot the function
plt.plot(x, y, label='Acos(x)')

# Naming the x and y axes
plt.xlabel('x')
plt.ylabel('Acos(x)')

# Giving a title to the graph
plt.title('Graph of Acos(x)')

# Adding a legend
plt.legend()

# Adding grid lines
plt.grid(True)

# Show the plot
plt.show()
