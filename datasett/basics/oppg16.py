import numpy as np
import matplotlib.pyplot as plt

vekt = np.random.normal(3.5, 0.9, 100)

plt.hist(vekt, bins=[2, 3, 4, 5, 6, 7], color="seagreen", edgecolor="black")
plt.xlabel("Vekt (kg)")
plt.ylabel("Antall")
plt.show()