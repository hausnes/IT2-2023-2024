# Laga av Knut Helge Dyvik, med nokre endringar av Jo Bjørnar

import csv

with open("utleige.csv", "r", encoding="utf-8") as input:
    content = csv.reader(input, delimiter=",")

    headers = next(content)

    rows = []
    for row in content:
        rows.append(row)

'''
    ------
    Del B
    ------
'''
min = int(rows[0][9])
max = int(rows[0][9])
summen = 0
count = 0

for row in rows:
    price = int(row[9])
    if price == 0:
        continue
    
    if price < min:
        min = price
    if price > max:
        max = price
    summen += price
    count += 1

avg = summen/count

print("Laveste pris:", min)
print("Høyeste pris:", max)
print("Gjennomsnittlig pris:", avg)

'''
    ------------------------
    Del C, v1 - treg løsning
    ------------------------
'''

# Lager dictionary med antall utleieobjekter per utleier
# hosts = {}

# for row in rows:
#     if row[3] not in hosts:
#         hosts[row[3]] = 1
#     else:
#         hosts[row[3]] += 1

# Lager liste med navn over alle utleiere og sorterer denne fra flest til færrest utleieobjekter
# hosts_sorted = []
# for host in hosts:
#     hosts_sorted.append(host)

# for i in range(len(hosts_sorted)):
#     max = i
#     for j in range(len(hosts_sorted)-i):
#         j += i
#         host = hosts_sorted[j]
#         max_host = hosts_sorted[max]

#         if hosts[host] > hosts[max_host]:
#             max = j

#     temp = hosts_sorted[max]
#     hosts_sorted[max] = hosts_sorted[i]
#     hosts_sorted[i] = temp

# for i in range(5):
#     print(hosts_sorted[i]+":", hosts[hosts_sorted[i]])

'''
    --------------------------------------------------------
    Del C - v2 - alternativ løsning på del C, som er raskere
    --------------------------------------------------------
'''
# Lager dictionary med antall utleieobjekter per utleier
hosts = {}

for row in rows:
    if row[3] not in hosts:
        hosts[row[3]] = 1
    else:
        hosts[row[3]] += 1

# Lager liste med navn over alle utleiere og sorterer denne fra flest til færrest utleieobjekter
hosts_sorted = sorted(hosts, key=hosts.get, reverse=True)

print("\nUtleiere:")
for i in range(5):
    print(hosts_sorted[i]+":", hosts[hosts_sorted[i]])

# Visualisering av data
import matplotlib.pyplot as plt

first_5_hosts = []

for i in range(5):
    first_5_hosts.append(hosts[hosts_sorted[i]])

plt.bar(hosts_sorted[:5], first_5_hosts)
plt.xlabel('"host_name"')
plt.ylabel("Antall utleieobjekter")
plt.show()

'''
    -------------------------------------------------------------------------------------
    Del D : Nabolag. NB: Her bør du se at dette er akkurat det samme, med andre data
    enn i del C, så du bør skrive en mer generell løsning som kan brukes for begge deler.
    -------------------------------------------------------------------------------------
''' 
# Samme som del C, men nå for nabolag
nabo = {}

for row in rows:
    if row[5] not in nabo:
        nabo[row[5]] = 1
    else:
        nabo[row[5]] += 1

# Lager liste med navn over alle utleiere og sorterer denne fra flest til færrest utleieobjekter
nabo_sorted = sorted(nabo, key=nabo.get, reverse=True)

print("\nNabolag:")
for i in range(5):
    print(nabo_sorted[i]+":", nabo[nabo_sorted[i]])

# Visualisering av data
import matplotlib.pyplot as plt

first_5_nabo = []

for i in range(5):
    first_5_nabo.append(nabo[nabo_sorted[i]])

plt.bar(nabo_sorted[:5], first_5_nabo)
plt.xlabel('"Neighbourhood"')
plt.ylabel("Antall utleieobjekter")
plt.xticks(rotation=90)
plt.subplots_adjust(bottom=0.4)
plt.show()

'''
    ------------------------
    Del E - kart
    ------------------------
'''

import folium as fol

# Sorterer listen basert på antall anmeldelser
rows_sorted = sorted(rows, key=lambda row: int(row[11]), reverse=True)

# Henter ut de fem objektene med flest anmeldelser
top_5_reviews = rows_sorted[:5]

points = [[float(object[6]), float(object[7])] for object in top_5_reviews]

# Beregner midtpunktet for alle punktene
middle = [sum(point[0] for point in points) / 5, sum(point[1] for point in points) / 5]

m = fol.Map(middle, zoom_start=11)

for point in points:
    fol.CircleMarker(point).add_to(m)

m.save("kart.html")