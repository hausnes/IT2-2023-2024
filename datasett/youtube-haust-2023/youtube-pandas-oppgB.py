import json
import pandas as pd
import matplotlib.pyplot as plt

# Last inn JSON-filen
with open('youtube.json', 'r') as f:
    data = json.load(f)

# Konverter JSON-data til ein Pandas DataFrame
df = pd.DataFrame(data)

# Rens data for eventuelle problematiske verdiar
df = df[df['Country'].notna() & df['Youtuber'].notna() & (df['Country'].str.lower() != 'nan')]

# Konverter 'subscribers' og 'video views' til numeriske verdiar
df['subscribers'] = pd.to_numeric(df['subscribers'], errors='coerce') # errors='coerce' gjer at alle ikkje-tal vert konvertert til NaN
df['video views'] = pd.to_numeric(df['video views'], errors='coerce')

# Grupper data etter land og beregn gjennomsnittleg antall abonnentar og videovisningar per kanal
grouped = df.groupby('Country').agg({'subscribers': 'mean', 'video views': 'mean'})

# Presenter resultata i ein barplot
fig, ax = plt.subplots(2, 1, figsize=(10, 10))

ax[0].bar(grouped.index, grouped['subscribers'])
ax[0].set_xlabel('Land')
ax[0].set_ylabel('Gjennomsnittleg antall abonnentar')
ax[0].set_title('Gjennomsnittleg tal på abonnentar per kanal, etter land')
ax[0].tick_params(axis='x', rotation=90)

ax[1].bar(grouped.index, grouped['video views'])
ax[1].set_xlabel('Land')
ax[1].set_ylabel('Gjennomsnittleg antall visningar')
ax[1].set_title('Gjennomsnittleg tal på visningar per kanal, etter land')
ax[1].tick_params(axis='x', rotation=90)

plt.subplots_adjust(bottom=0.15, hspace=0.5)
plt.show()