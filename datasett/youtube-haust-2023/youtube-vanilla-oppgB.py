import json
import matplotlib.pyplot as plt

filename = 'youtube.json'

# Finner encoding til filen (skrive av Birk)
with open(filename,'r') as f:
    filestr = str(f)
    index = filestr.find("encoding=")
    enc = filestr[index+9:].replace('\'', '')
    enc = enc.replace('>', '')
    f.close
    print("Encoding:")
    print(enc)
    
# Last inn JSON-filen
with open(filename, 'r', encoding=enc) as f:
    data = json.load(f)

# Rens data for eventuelle problematiske verdiar
cleaned_data = []
for d in data:
    if d['Country'] and d['Youtuber'] and d['Country'].lower() != 'nan':
        cleaned_data.append(d)

# Grupper data etter land og beregn gjennomsnittleg antall abonnentar og videovisningar per kanal
country_data = {}
for d in cleaned_data:
    if d['Country'] in country_data:
        country_data[d['Country']].append((d['subscribers'], d['video views']))
    else:
        country_data[d['Country']] = [(d['subscribers'], d['video views'])]

# Berekn gjennomsnittleg antall abonnentar og videovisningar per kanal for kvart land
average_data = {}
for country, values in country_data.items():
    total_subscribers = 0
    total_views = 0
    for subscribers, views in values:
        total_subscribers += subscribers
        total_views += views
    average_subscribers = total_subscribers / len(values)
    average_views = total_views / len(values)
    average_data[country] = (average_subscribers, average_views)

# Splitter land og antall til to separate lister for plotting
countries = []
average_subscribers = []
average_views = []
for country, values in average_data.items():
    countries.append(country)
    average_subscribers.append(values[0])
    average_views.append(values[1])

# Presenter resultata i ein barplot
fig, ax = plt.subplots(2, 1, figsize=(10, 10))

ax[0].bar(countries, average_subscribers)
ax[0].set_xlabel('Land')
ax[0].set_ylabel('Gjennomsnittleg antall abonnentar')
ax[0].set_title('Gjennomsnittleg tal på abonnentar per kanal, etter land')
ax[0].tick_params(axis='x', rotation=90)

ax[1].bar(countries, average_views)
ax[1].set_xlabel('Land')
ax[1].set_ylabel('Gjennomsnittleg antall visningar')
ax[1].set_title('Gjennomsnittleg tal på visningar per kanal, etter land')
ax[1].tick_params(axis='x', rotation=90)

plt.subplots_adjust(bottom=0.15, hspace=0.5)
plt.show()
