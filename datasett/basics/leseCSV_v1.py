# Eksempel frå boka, vha. csv-bibliotek
# Sjå v2 for korleis dette kunne blitt gjort vha pandas

import csv
import matplotlib.pyplot as plt

filnavn = "./datasett/basics/befolkning-voss.csv" # NB: Om du ikkje køyrer frå VS Code så må du fjerne alt unntatt befolkning-voss.csv

# Lister for å ta vare på alle årstall og befolkningsstørrelser
aarstall = []
befolkning = []

with open(filnavn, encoding="utf-8-sig") as fil:
  filinnhold = csv.reader(fil, delimiter=";")

  overskrifter = next(filinnhold)
  print(overskrifter)
  
  for rad in filinnhold:
    aarstall.append(int(rad[0]))
    befolkning.append(int(rad[1]))

# Tegner grafen
plt.plot(aarstall, befolkning)
plt.grid()
plt.show()