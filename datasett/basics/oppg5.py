'''
Tegn grafene til disse fire funksjonene i én felles figur:
y = 2x + 1
y = x2 – 3
y = 2x
y = x over 3
'''

import matplotlib.pyplot as plt
import numpy as np

xverdier = np.linspace(-10, 10, 100)

# Graf 1
yverdier1 = 2*xverdier + 1
plt.plot(xverdier, yverdier1, label='2x + 1')

# Graf 2
yverdier2 = xverdier**2 - 3
plt.plot(xverdier, yverdier2, label='x^2 - 3')

# Graf 3
yverdier3 = 2*xverdier
plt.plot(xverdier, yverdier3, label='2x')

# Graf 4
yverdier4 = xverdier / 3
plt.plot(xverdier, yverdier4, label='x/3')

plt.grid()

plt.legend()

plt.show()