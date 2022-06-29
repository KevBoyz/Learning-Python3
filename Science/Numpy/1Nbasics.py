import numpy as np
from matplotlib import pyplot as plt

"""
from random import randint
matrix = np.array([np.linspace(0, 10, 50), np.linspace(0, 10, 50),
                   np.linspace(0, 10, 50), np.linspace(0, 10, 50)])
matrix[0] = matrix[0] ** 2 * randint(-5, 5)
matrix[1] = matrix[1] ** 2.5 * randint(-5, 5)
matrix[2] = matrix[2] ** 3 * randint(-5, 5)
matrix[3] = matrix[3] ** 3.5 * randint(-5, 5)
"""
"""

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
"""


arr = np.arange(0, 100, 10).reshape(2, 5)
# print(arr, '\n')

rg = np.random.default_rng()
# print(rg.random((4, 3)))

lin = np.linspace(-10, 10, 6)
# print(lin)

zeros = np.zeros(shape=(3, 3, 3, 3))  # 4 dims  -- ones 0 -> 1
# print(zeros)

# print(np.empty((2, 5)))  # None empty values

prices = np.full(100, fill_value=np.nan)
prices[[0, 25, 60, -1]] = [80., 30., 75., 50.]
plt.plot([80., 30., 75., 50.])
# Linearly interpolate the missing values and add some noise.
x = np.arange(len(prices))
is_valid = ~np.isnan(prices)
prices = np.interp(x=x, xp=x[is_valid], fp=prices[is_valid])  # val, val i
print(prices)
prices += np.random.randn(len(prices))

fig, ax = plt.subplots()
ax.plot(prices)
plt.show()
