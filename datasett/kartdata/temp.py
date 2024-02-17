'''
started_at,ended_at,duration,start_station_id,start_station_name,start_station_description,start_station_latitude,start_station_longitude,end_station_id,end_station_name,end_station_description,end_station_latitude,end_station_longitude
2022-05-01 00:55:46.521000+00:00,2022-05-01 01:02:05.964000+00:00,379,450,Elisenberg,ved holdeplassen,59.919524,10.70884,429,Thune,ved bomringen,59.92208,10.68588
2022-05-01 03:00:17.214000+00:00,2022-05-01 03:10:10.317000+00:00,593,423,Schous plass,nærmest rundkjøringen,59.920335,10.760804,612,Ensjøveien,ved turvei,59.91662195885618,10.783309055819714
2022-05-01 03:02:31.181000+00:00,2022-05-01 03:09:50.019000+00:00,438,463,Schous plass trikkestopp,ved biblioteket,59.9207284,10.7594857,586,Københavngata busstopp,ved Fagerheim tennisklubb,59.9294565845173,10.769121495700826
'''
import pandas as pd

data = pd.read_csv("sykkel_mini.csv")
data = data[["started_at","start_station_name"]]
print(data.head())

# Initialiser to tomme lister
stasjoner = []
tall = []

# Gå gjennom hver rad i datasettet
for index, row in data.iterrows():
    # Hvis stasjonsnavnet allerede er i listen, øk det tilsvarende tallet med 1
    if row['start_station_name'] in stasjoner:
        index = stasjoner.index(row['start_station_name'])
        tall[index] += 1
    # Hvis stasjonsnavnet ikke er i listen, legg det til og legg til 1 i tall-listen
    else:
        stasjoner.append(row['start_station_name'])
        tall.append(1)

print(stasjoner)
print(tall)

# Alternativt, med dictionary
# Initialiser en tom dictionary
stasjoner = {}

# Gå gjennom hver rad i datasettet
for index, row in data.iterrows():
    # Hvis stasjonsnavnet allerede er i dictionary, øk tallet med 1
    if row['start_station_name'] in stasjoner:
        stasjoner[row['start_station_name']] += 1
    # Hvis stasjonsnavnet ikke er i dictionary, legg det til med tallet 1
    else:
        stasjoner[row['start_station_name']] = 1

# Konverter dictionary til to lister
liste = list(stasjoner.keys())
tall = list(stasjoner.values())

print(liste)
print(tall)