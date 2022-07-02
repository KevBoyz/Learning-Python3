from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(2, 8*np.pi, 400)
fig, axs = plt.subplots(3)

y = np.sin(x)

plt.subplot(1, 2, 1)
plt.plot(x, y, color='#ff0000')

plt.plot(x, y)

y = np.cos(x)

plt.subplot(1, 2, 2)
plt.plot(x, y, color='#ff0000')


plt.show()

