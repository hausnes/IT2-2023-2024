import json

f = open("countries.json", "r") # OBS: Spør om du får feilmelding her
land = json.loads(f.read())
print(land)

# Iterer gjennom alle landene i landet
for l in land:
    print(l["name"]["common"])