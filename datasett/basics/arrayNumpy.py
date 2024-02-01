'''
    En array er omtrent som en liste, men en viktig forskjell er at vi kan utføre matematiske operasjoner 
    på hvert enkelt av elementene i arrayen. Vi kan for eksempel gange alle verdier i en array med 2. Vi 
    finner arrayer-funksjoner i biblioteket «numpy».
    
    Vi kan først lage en array med x-verdier ved hjelp av linspace() . Da kan vi angi hvilken x-verdi vi 
    skal starte på, hvilken x-verdi vi skal slutte på, og hvor mange x-verdier vi ønsker totalt.
'''

import matplotlib.pyplot as plt
import numpy as np

def f(x):
  return x**2

xverdier = np.linspace(0, 10, 20) # 20 verdier mellom 0 og 10
print(xverdier) # NB: 11 verdier, frå 0 til og med 10
yverdier = f(xverdier)

plt.plot(xverdier, yverdier)
plt.show()