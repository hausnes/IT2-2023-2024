import csv

def read_csv_file(file_path, enc):
    with open(file_path, 'r', encoding=enc) as file:
        reader = csv.reader(file, delimiter=';')
        print(f"Endte opp med encoding: {enc}") # For å sjå kva encoding som blei nytta for å få det til å fungere
        for row in reader:
            print(row)

try:
    read_csv_file('data.csv', 'utf-8')
except UnicodeDecodeError:
    try:
        read_csv_file('data.csv', 'ISO-8859-1')
    except UnicodeDecodeError:
        read_csv_file('data.csv', 'cp1252')