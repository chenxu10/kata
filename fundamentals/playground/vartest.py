import numpy as np
import matplotlib.pyplot as plt

# Define the number of steps and probability of going up
n_steps = 1000
p_up = 0.5

# Generate the steps using a geometric random variable
steps = np.random.geometric(p_up, size=n_steps) - 1

# Calculate the cumulative sum of the steps and add the starting value of 1
walk = np.cumprod(1 + steps)

# Plot the random walk
plt.plot(walk)
plt.title('Geometric Random Walk')
plt.xlabel('Number of Steps')
plt.ylabel('Value')
plt.show()