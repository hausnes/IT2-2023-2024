import json

def tolke(data):
    for linje in data:
        print(linje)

def read_json_file(file_path, enc):
    with open(file_path, 'r', encoding=enc) as file:
        next(file) # Hoppar over linje 1
        data = json.load(file)
        print(f"Encoding: {enc}")  # For å sjå kva encoding som blei nytta
        #print(data)
        tolke(data)

try:
    read_json_file('data.json', 'utf-8')
except UnicodeDecodeError:
    try:
        read_json_file('data.json', 'ISO-8859-1')
    except UnicodeDecodeError:
        read_json_file('data.json', 'cp1252')