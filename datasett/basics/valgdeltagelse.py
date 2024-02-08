import matplotlib.pyplot as plt

år = []
deltagelse = []

filnavn = "valgdeltagelse.txt"

with open(filnavn) as fil:
  for linje in fil:
    linjeTemp = linje.rstrip().split(",")

    år.append(int(linjeTemp[0]))
    deltagelse.append(float(linjeTemp[1]))

print(år)
print(deltagelse)