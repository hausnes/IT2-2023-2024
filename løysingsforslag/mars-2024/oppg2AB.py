import csv
import matplotlib.pyplot as plt

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    # Opprettar ei ordbok for å halde styr på kor mange utøvarar som er i kvar aldersgruppe
    counter = {'18 - 34': 0, '35 - 54': 0, '55 +': 0}
    # Tel opp kor mange utøvarar som er i kvar aldersgruppe
    for row in reader:
        if row['age_group'] in counter:
            counter[row['age_group']] += 1

# For å gjere det lettare å lage eit søylediagram, kan me lage to lister av ordboka
age_groups = list(counter.keys())
print(f"Testutskrift for å sjå kva me har per no, først gruppene: \n{age_groups}")
counts = list(counter.values())
print(f"Deretter, antallet utøvarar: \n{counts}")

print()

# Går gjennom listene og skriv ut kor mange utøvarar som er i kvar aldersgruppe, jfr. oppgåvetekst
for i in range(len(age_groups)):
    print(f"I aldersgruppa {age_groups[i]} er det {counts[i]} utøvarar.")

# Lagar søylediagram
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.title('Count of each Age Group')
plt.ticklabel_format(style='plain') # Unngår den litt forvirrande bruken av vitenskapelig format
plt.bar(age_groups, counts)
plt.show()

# NB: Det er ein feil her - då det er ein repetisjon for alle vekene.. Fiks gjerne denne sjølv. 
# Du treng altså berre sjå på veke 1.