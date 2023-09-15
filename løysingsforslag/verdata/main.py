import verdata
import datetime as dt
import matplotlib.pyplot as plt

ver = verdata.verdata

# Plotting av temperatur
x = []
y = []

for dag in ver["daily"]:
    unixtid = dag["dt"]
    dato = dt.datetime.fromtimestamp(unixtid) # Konverterer unix-tid til dato
    temperatur = dag["temp"]["day"] - 273.15
    print(f"Varsel for {dato}. Temperatur: {temperatur:5.2f} grader celsius.")
    x.append(dato)
    y.append(temperatur)

    ver = dag["weather"]
    for v in ver:
        beskrivelse = v["description"]
        print("Beskrivelse: " + beskrivelse)

plt.plot(x,y)
plt.title("Temperaturvarsel")
plt.xlabel("Dato")
plt.ylabel("Temperatur (C)")
plt.grid()
plt.xticks(rotation=90) # Skriv dato nedover slik at det er synlig
plt.show()

'''
for dag in ver["daily"]:
    print(f"\nDag: {dag}")
'''