import json

with open('data.json', 'r', encoding='utf-8') as file:
    next(file)  # Hopp over første linje
    data = json.load(file)  # Last resten av innhaldet

    print(data)