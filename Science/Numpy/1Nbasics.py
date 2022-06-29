import numpy as np
from matplotlib import pyplot as plt
import scipy.interpolate as interpolate

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
days = np.arange(len(prices))
is_valid = ~np.isnan(prices)
prices = np.interp(x=days, xp=days[is_valid], fp=prices[is_valid])  # val, val i
prices += np.random.randn(len(prices)) * 2

fig, ax = plt.subplots()
ax.plot(prices)
ax.plot(prices, 'bo')
# plt.show()


y = np.random.random(20)
x = np.arange(0, y.size)

new_length = 80
new_x = np.linspace(x.min(), x.max(), new_length)
new_y = interpolate.interp1d(x, y, kind='linear')(new_x)

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(x, y, 'ro-')
plt.subplot(2, 1, 2)
plt.plot(new_x, new_y, 'bo-')
plt.show()
