# https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data/data
# id,name,host_id,host_name,neighbourhood_group,neighbourhood,latitude,longitude,room_type,price,minimum_nights,number_of_reviews,last_review,reviews_per_month,calculated_host_listings_count,availability_365
# Host med flest listings
# Neighbourhood med flest listings
# Dyraster listing
# Billigaste listing
# Kva nabolag kjem høgast ut med tanke på antallet listings, og pris?
# Mest populære romtype
# Mest populære nabolag

# Teikn inn dei 5 mest populære nabolaga på eit kart

import csv
import matplotlib.pyplot as plt

fil = 'airbnb.csv'

with open(fil, encoding='utf-8') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    listings = []
    for row in reader:
        listings.append(row)

print(header_row)

# Skrive ny linje til CSV-fila
ny = [999999,"Hausnesgarden",2787,"Jobis","Granvin",40.64749,-73.97237,"Private room",149,1,9,2018-10-19,0.21,6,365]
with open(fil, 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(ny)