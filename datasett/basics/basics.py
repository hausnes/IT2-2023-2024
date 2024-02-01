import matplotlib.pyplot as plt

# Graf nr. 1
xverdier = [0, 1, 2, 3, 4]   # Liste med x-verdier
yverdier = [0, 1, 4, 9, 16]  # Liste med y-verdier

# Graf nr. 2
y2 = [16, 9, 4, 1, 0]

# Graf nr. 3
y3 = [10, 10, 10, 10, 10]

# Lager grafen
plt.plot(xverdier, yverdier, label="Stigande")  # Lager første linje
plt.plot(xverdier, y2, label="Synkande")              # Lager andre linje
plt.scatter(xverdier, y3, label="Konstant")              # Lager tredje linje
plt.legend()                                    # Viser labels
plt.show()                                      # Viser grafene