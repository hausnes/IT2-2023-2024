import pandas as pd
import matplotlib.pyplot as plt

filnavn = "./datasett/basics/befolkning-voss.csv"

# Les inn CSV-fila med pandas
data = pd.read_csv(filnavn, delimiter=";", encoding="utf-8-sig")

print(data.describe())

# Hent ut årstall og befolkning som lister
aarstall = data['År'].tolist()
# aarstall = data.iloc[:, 0].tolist() # Alternativ
befolkning = data['Befolkning'].tolist()
# befolkning = data.iloc[:, 1].tolist() # Alternativ

# Tegner grafen
plt.plot(aarstall, befolkning)
plt.grid()
plt.show()

# Ekstra, om variasjon i datasettet

# Beregn endringen i befolkningen fra år til år
data['Befolkningsendring'] = data['Befolkning'].diff()

# Tegn en graf over befolkningsendringen
plt.plot(data['År'], data['Befolkningsendring'])
plt.grid()
plt.show()