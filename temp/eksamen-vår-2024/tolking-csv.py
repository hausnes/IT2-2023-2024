import csv
import matplotlib.pyplot as plt

def read_csv_file(file_path, enc):
    with open(file_path, 'r', encoding=enc) as file:
        print(f"Encoding: {enc}")  # For å sjå kva encoding som blei nytta
        
        # csv.reader for å kunne hoppe over dei to første linjene
        reader = csv.reader(file, delimiter=';')
        next(reader)
        next(reader)

        # Bruker deretter csv.DictReader
        reader = csv.DictReader(file, delimiter=';')
        data = list(reader)
        tolke(data)

def tolke(data):
    summary = summarize_data(data)

    # Skriv ut oppsummeringen
    for (activity, gender), time_spent in summary.items():
        print(f"Aktivitet: {activity}, Kjønn: {gender}, Tid brukt: {time_spent}")

    plot_data(summary)

    # Vis en stolpediagram av oppsummeringen
    plot_data(summary)

def summarize_data(data):
    summary = {}

    for item in data:
        # Hent aktivitet og kjønn
        activity = item['alle aktiviteter']
        gender = item['kjønn']

        # Sjekk om aktiviteten er en underkategori
        if not activity.startswith('*'):
            continue

        # Dersom kombinasjonen av kjønn og aktivitet ikkje er i summary, legg det til
        if (activity, gender) not in summary:
            summary[(activity, gender)] = 0

        # Legg til tid brukt i oppsummeringen
        summary[(activity, gender)] += float(item['Tidsbruk 2000 I alt'])

    return summary

def plot_data(summary):
    genders = ['Menn', 'Kvinner']
    times = [sum(time for (activity, gender), time in summary.items() if gender == g) for g in genders]

    plt.bar(genders, times)
    plt.xlabel('Kjønn')
    plt.ylabel('Total tid brukt')
    plt.title('Total tid brukt av hvert kjønn')
    plt.show()

try:
    read_csv_file('data.csv', 'utf-8')
except UnicodeDecodeError:
    try:
        read_csv_file('data.csv', 'ISO-8859-1')
    except UnicodeDecodeError:
        read_csv_file('data.csv', 'cp1252')