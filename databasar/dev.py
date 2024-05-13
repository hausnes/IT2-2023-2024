# CSV og JSON opp mot databaser og SQL
# - utforske og vurdere alternative løsninger for design og implementering av et program
# - gjøre rede for standarder for lagring, utveksling og sikring av ulike typer data
# - bruke programmering til å innhente, analysere og presentere informasjon fra reelle datasett

import csv
#from collections import Counter

with open('dev_bruk.csv', 'r') as file:
    reader = csv.DictReader(file)
    counts = {} # Klargjer ei tom ordbok (dictionary)
    #counts = Counter()

    for row in reader:
        fav = row["language"]
        if fav in counts:
            counts[fav] += 1
        else:
            counts[fav] = 1   
        #counts[fav] += 1

# Utskrift, usortert
print(counts)

# Sortering
for fav in sorted(counts, key=counts.get, reverse=True):
    print(fav, counts[fav])

# SQL
# .\sqlite3.exe mindb.db
# sqlite> .mode csv
# sqlite> .import dev_bruk.csv spraak
# sqlite> .schema
# sqlite> SELECT * FROM spraak;
# sqlite> SELECT COUNT(*) FROM spraak WHERE language = 'Python';
# sqlite> SELECT COUNT(*) FROM spraak WHERE language = 'JS' AND area = 'Frontend';
# sqlite> SELECT language, COUNT(*) FROM spraak GROUP BY language ORDER BY COUNT(*) DESC;
# sqlite> SELECT language, area, COUNT(*) FROM spraak GROUP BY area ORDER BY COUNT(*);