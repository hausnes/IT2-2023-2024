import json
import matplotlib.pyplot as plt

# Finner encodingen til filen
with open(filepath,'r') as f:
    filestr = str(f)
    index = filestr.find("encoding=")
    enc = filestr[index+9:].replace('\'', '')
    enc = enc.replace('>', '')
    f.close

# Last inn JSON-fila
with open('youtube.json', 'r', encoding=enc) as f:
    data = json.load(f)

# Rens data for eventuelle problematiske verdiar
cleaned_data = []
for d in data:
    if d['Country'] and d['Youtuber'] and d['Country'].lower() != 'nan':
        cleaned_data.append(d)

# Grupper data etter land og tell antall YouTube-kanalar
country_counts = {}
for d in cleaned_data:
    if d['Country'] in country_counts:
        country_counts[d['Country']] += 1
    else:
        country_counts[d['Country']] = 1

# Velg dei ti landa med flest YouTube-kanalar
top_countries = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)[:10]

# Splitter land og antall til to separate lister for plotting
countries = []
counts = []
for country, count in top_countries:
    countries.append(country)
    counts.append(count)

# Eventuelt kan du "unzippe", der du konverterer ei liste av tuplar til separate lister.
# countries, counts = zip(*top_countries)

# Presenter resultata i ein barplot
plt.figure(figsize=(10, 5))
plt.bar(countries, counts)
plt.xlabel('Land')
plt.ylabel('Antall YouTube-kanalar')
plt.title('Topp 10 land med flest YouTube-kanalar')

# Roter x-aksen sine etikettar 45 grader
plt.xticks(rotation=45)

# Juster plasseringen av x-aksen sine etikettar (= meir plass til etikettane)
plt.subplots_adjust(bottom=0.28)

plt.show()
