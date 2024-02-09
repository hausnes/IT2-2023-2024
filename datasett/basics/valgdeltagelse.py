import matplotlib.pyplot as plt

år = []
deltagelse = []

filnavn = "valgdeltagelse.txt"

with open(filnavn) as fil:
  for linje in fil:
    linjeTemp = linje.rstrip().split(";")
    print(linjeTemp)
    år.append(int(linjeTemp[0]))
    deltagelse.append(float(linjeTemp[1].replace(",",".")))

print(år)
print(deltagelse)

plt.plot(år,deltagelse)
plt.grid()
plt.show()