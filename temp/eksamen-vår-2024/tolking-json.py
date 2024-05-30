import json
import pandas as pd
import re

# def identifiser_subkategori(data):
#     for item in data:
#         if '�' in item['alle aktiviteter']:
#             # print("Fant spesialteikn..")
#             # item['underkategori'] = item['alle aktiviteter'].replace('�', '').strip()
#             re.sub(r'\W+', ' ', item['alle aktiviteter'])

def tolkePandas(data):
    # for linje in data: # For testing
    #     print(linje)

    # Konverterer til dataframe
    df = pd.DataFrame(data)

    # Grupperer data basert på kjønn og aktivitet, og summerer tida brukt
    summary = df.groupby(['kjønn', 'alle aktiviteter'])['Tidsbruk 2000 I alt'].sum()

    # Print the summary
    print(summary)

def tolke(data):
    summary = {}

    for item in data:
        # Hent aktivitet og kjønn
        activity = item['alle aktiviteter']
        gender = item['kjønn']

        # Dersom kombinasjonen av kjønn og aktivitet ikkje er i summary, legg det til
        if (activity, gender) not in summary:
            summary[(activity, gender)] = 0

        # Legg til tid brukt i oppsummeringen
        summary[(activity, gender)] += item['Tidsbruk 2000 I alt']

    # Skriv ut oppsummeringen
    for (activity, gender), time_spent in summary.items():
        print(f"Aktivitet: {activity}, Kjønn: {gender}, Tid brukt: {time_spent}")

# Leser data inn
def read_json_file(file_path, enc):
    with open(file_path, 'r', encoding=enc) as file:
        next(file) # Hoppar over linje 1
        data = json.load(file)
        print(f"Encoding: {enc}")  # For å sjå kva encoding som blei nytta
        #identifiser_subkategori(data)
        #print(data)
        tolke(data)

try:
    read_json_file('05994_20240126-145813-json.json', 'utf-8')
except UnicodeDecodeError:
    try:
        read_json_file('05994_20240126-145813-json.json', 'ISO-8859-1')
    except UnicodeDecodeError:
        read_json_file('05994_20240126-145813-json', 'cp1252')