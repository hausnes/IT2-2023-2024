import osmnx as ox
import folium as fol

import csv
import matplotlib.pyplot as plt

punkter = []

with open('sykkel.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        punkter.append([float(row['end_station_latitude']), float(row['end_station_longitude'])])

# Lager et kart
m = fol.Map([59.911491, 10.757933], zoom_start=12) # Midtpunkt Oslo, og godt zooma ut

# Legger til byene
for punkt in punkter: # NB: Dette blir SÆRS mange punkt og teikne inn, og HTML-fila blir gigantisk. Derfor: Finn ein egna måte å optimalisere dette på.
  fol.CircleMarker(punkt).add_to(m)

# Lagrer kartet
m.save("oslo_sykkel.html")