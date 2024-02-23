import json

# Load the data from the file
with open('youtube.json', 'r') as f:
    data = json.load(f)

for item in data:
    # Skriv ut alle kanalar og kor mange visningar dei har
    print(f"{item['Title']} har {item['video views']} visningar.")
    
    # Finn "video views" med problematisk data (0, ikkje eit tall, negativt tal osv.)
    views = item.get('video views', None)
    if views is None or str(views).lower() == 'nan' or not str(views).isdigit() or int(views) <= 0:
        print(f"Problematiske data funne for: {item['Title']}, med antall visningar: {views}.")
    
    # Merk at du kunne gått meir tradisjonelt til verks med item['video views'] i staden for item.get('video views', None)
    # Dette vil derimot kunne gje ein KeyError dersom 'video views' ikkje finst i datasettet, medan item.get('video views', None) vil returnere None
    if item['video views'] is None or str(item['video views']).lower() == 'nan' or not str(item['video views']).isdigit() or int(item['video views']) <= 0:
        print(f"Problematiske data funne for: {item['Title']}, med antall visningar: {item['video views']}.")