import json
import pandas as pd
import matplotlib.pyplot as plt

# Last inn JSON-filen
with open('youtube.json', 'r') as f:
    data = json.load(f)

# Konverter JSON-data til ein Pandas DataFrame
df = pd.DataFrame(data)

# Rens data for eventuelle problematiske verdiar og legg til i ny DataFrame:
# Fjern rader med manglande data for 'Country' og 'Youtuber', samt utelukk rader der 'Country' er 'nan'.
# notna() er ein Pandas-metode som returnerer ein boolsk verdi som er True for alle ikkje-manglande verdiar.
df = df[df['Country'].notna() & df['Youtuber'].notna() & (df['Country'].str.lower() != 'nan')]

# Grupper data etter land og tell antall YouTube-kanalar
country_counts = df['Country'].value_counts()

# Velg dei ti landa med flest YouTube-kanalar
top_countries = country_counts[:10]

# Presenter resultata i ein barplot
plt.figure(figsize=(10, 5))
plt.bar(top_countries.index, top_countries.values)
plt.xlabel('Land')
plt.ylabel('Antall YouTube-kanalar')
plt.title('Topp 10 land med flest YouTube-kanalar')

# Roter x-aksen sine etikettar 45 grader
plt.xticks(rotation=45)

# Juster plasseringen av x-aksen sine etikettar (= meir plass til etikettane)
plt.subplots_adjust(bottom=0.28)

plt.show()