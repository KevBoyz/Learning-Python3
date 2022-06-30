from random import randint
import numpy as np
from matplotlib import pyplot as plt

matrix = np.array([np.linspace(0, 10, 50), np.linspace(0, 10, 50),
                   np.linspace(0, 10, 50), np.linspace(0, 10, 50)])
matrix[0] = matrix[0] ** 2 * randint(-5, 5)
matrix[1] = matrix[1] ** 2.5 * randint(-5, 5)
matrix[2] = matrix[2] ** 3 * randint(-5, 5)
matrix[3] = matrix[3] ** 3.5 * randint(-5, 5)

plt.plot(matrix[0], color='blue')
plt.plot(matrix[0], 'ro', color='blue')
plt.plot(matrix[1], color='green')
plt.plot(matrix[1], 'ro', color='green')
plt.plot(matrix[2], color='red')
plt.plot(matrix[2], 'ro', color='red')
plt.plot(matrix[2] - matrix[1], color='orange')
plt.plot(matrix[2] - matrix[1], 'ro', color='orange')
plt.plot(matrix[3], color='purple')
plt.plot(matrix[3], 'ro', color='purple')
plt.plot(matrix[3] - matrix[2], color='pink')
plt.plot(matrix[3] - matrix[2], 'ro', color='pink')
plt.show()
