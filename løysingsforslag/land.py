land = [
    {"Land" : "Norge"  , "Hovedstad" : "Oslo",      "Innbyggere": 5391369,  "Fylker": 18},
    {"Land" : "Sverige", "Hovedstad" : "Stockholm", "Innbyggere": 10099265, "Fylker": 21}
]

for x in land:
    country = x["Land"]
    innbyggere = x["Innbyggere"]
    print(f"Landet {country} har {x['Innbyggere']} innbyggere")