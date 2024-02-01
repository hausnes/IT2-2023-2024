import matplotlib.pyplot as plt
import numpy as np

xverdier = np.linspace(0, 20, 50)

# Graf 1
yverdier1 = 0.5*xverdier**2 
plt.plot(xverdier, yverdier1, label='0.5x^2')

# Graf 2
yverdier2 = -0.3*xverdier**3 
plt.plot(xverdier, yverdier2, label='-0.3x^3')

plt.grid()

plt.legend()

plt.show()