'''
    --------------------
     Ordbok (dictionary)
    --------------------
'''
print("Ordbok/dictionary:")
person = {"navn": "Jo Bjørnar Hausnes", "alder": 41}
print("All informasjon:", person)
print("Utvalt informasjon:",person["navn"])
# Legg til eit element i ordboka
person["adresse"] = "Hausnesvegen 25"
print("All oppdatert informasjon:", person)

# Liste med ordbok
print("\nListe med ordbok:")
personer = [
    {"navn": "Jo Bjørnar Hausnes", "alder": 41},
    {"navn": "Kari Nordmann", "alder": 42}
]

print("Løkke som går gjennom all informasjon:", personer)
# Løkke som går gjennom alle personane i lista
for person in personer:
    print("Fornavn:", person["navn"])

# Dictionary med personar og karakterar, der sistnemnte ligg i liste
dictPersonKarakterar = {
    "Jo Bjørnar Hausnes" : [4,5,5],
    "Rannveig Fluge Hausnes" : [5,6,6]
}

print("\nAlle elevar med karakterar:",dictPersonKarakterar)

print("\nHent ut om aktuell person:",dictPersonKarakterar.get("Rannveig Fluge Hausnes"))

leitEtter = input("Kven vil du leite etter? ")
#if dictPersonKarakterar.get(leitEtter) != "None":
#    print("Fant personen!")
person = dictPersonKarakterar.get(leitEtter,"Fant ikkje personen")
print(person)

# Slette ein person frå dictionary
slettPerson = input("Kven vil du slette? ")
if slettPerson in dictPersonKarakterar:
    dictPersonKarakterar.pop(slettPerson)
else:
    print("Fant ikkje personen")

print("\nAlle personar etter sletting:",dictPersonKarakterar)

# Meir om løkker og ordbøker
personInfo = {
  "fornavn": "Per", 
  "etternavn": "Christensen"
}

for x in personInfo:
    print(f"{x}:{personInfo.get(x)}")

for noekkel, verdi in personInfo.items():
    print(f"Nøkkel: {noekkel}, verdi: {verdi}.")

# Eksempel om sommar-OL:
sommer_ol = [
  { "årstall": 2004, "vinnertider": { "100 m": 10.93, "200 m": 22.06, "400 m": 49.41 } },
  { "årstall": 2008, "vinnertider": { "100 m": 10.78, "200 m": 21.74, "400 m": 49.62 } },
  { "årstall": 2012, "vinnertider": { "100 m": 10.75, "200 m": 21.88, "400 m": 49.55 } },
  { "årstall": 2016, "vinnertider": { "100 m": 10.71, "200 m": 21.78, "400 m": 49.44 } },
  { "årstall": 2020, "vinnertider": { "100 m": 10.61, "200 m": 21.53, "400 m": 48.36 } }
]

for ol in sommer_ol:
    print("\n",ol)

for ol in sommer_ol:
    aar = ol["årstall"]
    vinnertid_100m = ol["vinnertider"]["100 m"]
    print(f"I {aar} var vinnertiden på 100 m: {vinnertid_100m}.")