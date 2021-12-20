import numpy as np

a = np.arange(10).reshape(2, 5)
print(a ** 2, '\n')
print('Array values:')
print('a[0] =', a[0])
print('a[0][0] =', a[0][3])

rg = np.random.default_rng()
print(rg.random((2, 3)))




