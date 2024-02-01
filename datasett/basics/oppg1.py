'''
    I denne oppgaven skal du tegne grafen til funksjonen f(x) = 4x3 – x5 
    for x-verdier mellom –2 og 2 på minst to forskjellige måter. Du skal både bruke 
    lister som du fyller, og linspace() for å lage x-verdiene. 
    Du skal variere antall x-verdier og tegne grafen flere ganger. 
    Tegn grafene både med punkter og linjer. Bruk disse antallene:
    - 5
    - 10
    - 20
    - 50
'''

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 4*x**3 - x**5

xverdier = np.linspace(-2, 2, 50)
yverdier = f(xverdier)

plt.plot(xverdier, yverdier, label="Plott med 50 verdier", color="green")
plt.scatter(xverdier, yverdier, label="Scatter", color="red")
plt.title(r"Grafen til $f(x)=4x^{3}-x^{5}$")
plt.legend()
plt.show()