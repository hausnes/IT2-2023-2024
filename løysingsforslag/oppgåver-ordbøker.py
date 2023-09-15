'''
Oppgåve 1 (oppgåver frå lærebok, Aschehoug, kapittel om ordbøker - heilt til slutt)

'''

# Opprett en ordbok som inneholder tallene som nøkler og tekstene som verdier
tall_tekst = {
    1: "en", 
    2: "to", 
    3: "tre", 
    4: "fire", 
    5: "fem", 
    6: "seks", 
    7: "syv", 
    8: "åtte", 
    9: "ni", 
    10: "ti"
}

# Skriv ut alle tallene med sine tilhørende tekster i tabellform
print("Tall | Tekst")
print("-----|------")
for tall, tekst in tall_tekst.items():
    print(f"{tall:<5}| {tekst}")

# Test ordboka ved å la en bruker skrive inn et tall
tall_inn = int(input("Skriv inn et tall mellom 1 og 10: "))
if tall_inn in tall_tekst:
    print(f"Teksten for {tall_inn} er {tall_tekst[tall_inn]}.")
else:
    print(f"Ugyldig tall. Prøv igjen.")

'''
Oppgåve 2

'''

# Opprett en ordbok over norske byer
norske_byer = {
    "Oslo": {
        "innbyggere": 697899, 
        "fylke": "Oslo", 
        "landemerker": ["Holmenkollen", "Vigelandsparken", "Operaen"] 
    },
    "Bergen": {
        "innbyggere": 298969, 
        "fylke": "Vestland", 
        "landemerker": ["Bryggen", "Fløyen", "Fisketorget"] 
    },
    "Trondheim": {
        "innbyggere": 209462, 
        "fylke": "Trøndelag", 
        "landemerker": ["Nidarosdomen", "Tyholttårnet", "Gamle Bybro"] 
    },
    "Stavanger": {
        "innbyggere": 148289, 
        "fylke": "Rogaland", 
        "landemerker": ["Preikestolen", "Oljemuseet", "Domkirken"] 
    }
}

# Skriv ut all informasjonen om alle byene på en oversiktlig måte
for by, info in norske_byer.items():
    print(f"By: {by}")
    print(f"Innbyggere: {info['innbyggere']}")
    print(f"Fylke: {info['fylke']}")
    print(f"Landemerker: {', '.join(info['landemerker'])}")
    print()

'''
Oppgåve 3

'''

eliteserielag = [
    { "lag": "Lillestrøm", "seriemesterskap": [1976, 1977, 1986, 1989], "norgesmesterskap": [1977, 1978, 1981, 1985, 2007, 2017] },
    { "lag": "Molde", "seriemesterskap": [2011, 2012, 2014, 2019], "norgesmesterskap": [1994, 2005, 2013, 2014, 2021] },
    { "lag": "Viking", "seriemesterskap": [1972, 1973, 1974, 1975, 1979, 1982, 1991], "norgesmesterskap": [1979, 1989, 2001, 2019] },
    { "lag": "Strømsgodset", "seriemesterskap": [1970, 2013], "norgesmesterskap": [1969, 1970, 1973, 1991, 2010] },
    { "lag": "Aalesund", "seriemesterskap": [], "norgesmesterskap": [2009, 2011] },
    { "lag": "Rosenborg", "seriemesterskap": [1967, 1969, 1971, 1985, 1988, 1990, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2006, 2009, 2010, 2015, 2016, 2017, 2018], "norgesmesterskap": [1964, 1971, 1988, 1990, 1992, 1995, 1999, 2003, 2015, 2016, 2018] },
    { "lag": "Sarpsborg", "seriemesterskap": [], "norgesmesterskap": [] },
    { "lag": "Bodø/Glimt", "seriemesterskap": [2020, 2021], "norgesmesterskap": [1975, 1993] },
    { "lag": "Odd", "seriemesterskap": [], "norgesmesterskap": [2000] },
    { "lag": "Tromsø", "seriemesterskap": [], "norgesmesterskap": [1986, 1996] },
    { "lag": "Vålerenga", "seriemesterskap": [1965, 1981, 1983, 1984, 2005], "norgesmesterskap": [1980, 1997, 2002, 2008] },
    { "lag": "HamKam", "seriemesterskap": [], "norgesmesterskap": [] },
    { "lag": "Sandefjord", "seriemesterskap": [], "norgesmesterskap": [] },
    { "lag": "Haugesund", "seriemesterskap": [], "norgesmesterskap": [] },
    { "lag": "Jerv", "seriemesterskap": [], "norgesmesterskap": [] },
    { "lag": "Kristiansund", "seriemesterskap": [], "norgesmesterskap": [] }
]

# Opprett en liste over lagene som har vunnet minst ett seriemesterskap
seriemestere = []
for lag in eliteserielag:
    if len(lag["seriemesterskap"]) > 0:
        seriemestere.append(lag["lag"])

# Skriv ut listen over seriemestere
print("Lagene som har vunnet minst ett seriemesterskap er:")
print(", ".join(seriemestere))

# Opprett en liste over lagene som har vunnet minst ett norgesmesterskap
norgesmestere = []
for lag in eliteserielag:
    if len(lag["norgesmesterskap"]) > 0:
        norgesmestere.append(lag["lag"])

# Skriv ut listen over norgesmestere
print("Lagene som har vunnet minst ett norgesmesterskap er:")
print(", ".join(norgesmestere))

# Opprett en liste over lagene som har vunnet minst ett seriemesterskap og ett norgesmesterskap
dobbelvinnere = []
for lag in eliteserielag:
    if len(lag["seriemesterskap"]) > 0 and len(lag["norgesmesterskap"]) > 0:
        dobbelvinnere.append(lag["lag"])

# Skriv ut listen over dobbelvinnere
print("Lagene som har vunnet minst ett seriemesterskap og ett norgesmesterskap er:")
print(", ".join(dobbelvinnere))

# Finn laget som har vunnet serien flest ganger
max_serie = 0 # Antall seriemesterskap for det beste laget
beste_lag_serie = "" # Navnet på det beste laget i serien
for lag in eliteserielag:
    if len(lag["seriemesterskap"]) > max_serie:
        max_serie = len(lag["seriemesterskap"])
        beste_lag_serie = lag["lag"]

# Skriv ut navnet på det beste laget i serien
print(f"Laget som har vunnet serien flest ganger er {beste_lag_serie} med {max_serie} titler.")

# Finn laget som har vunnet norgesmesterskapet flest ganger
max_norge = 0 # Antall norgesmesterskap for det beste laget
beste_lag_norge = "" # Navnet på det beste laget i norgesmesterskapet
for lag in eliteserielag:
    if len(lag["norgesmesterskap"]) > max_norge:
        max_norge = len(lag["norgesmesterskap"])
        beste_lag_norge = lag["lag"]

# Skriv ut navnet på det beste laget i norgesmesterskapet
print(f"Laget som har vunnet norgesmesterskapet flest ganger er {beste_lag_norge} med {max_norge} titler.")

# Finn laget som vant serien første gang
min_aar_serie = 9999 # Det tidligste året for et seriemesterskap
første_lag_serie = "" # Navnet på det første laget som vant serien
for lag in eliteserielag:
    if len(lag["seriemesterskap"]) > 0 and min(lag["seriemesterskap"]) < min_aar_serie:
        min_aar_serie = min(lag["seriemesterskap"])
        første_lag_serie = lag["lag"]

# Skriv ut navnet på det første laget som vant serien
print(f"Laget som vant serien første gang var {første_lag_serie} i {min_aar_serie}.")

# Finn laget som vant serien sist
max_aar_serie = 0 # Det seneste året for et seriemesterskap
siste_lag_serie = "" # Navnet på det siste laget som vant serien
for lag in eliteserielag:
    if len(lag["seriemesterskap"]) > 0 and max(lag["seriemesterskap"]) > max_aar_serie:
        max_aar_serie = max(lag["seriemesterskap"])
        siste_lag_serie = lag["lag"]

# Skriv ut navnet på det siste laget som vant serien
print(f"Laget som vant serien sist var {siste_lag_serie} i {max_aar_serie}.")

# Eksempel 
personer = {
    "jb.hausnes@gmail.com": {
        "fornavn": "Jo Bjørnar", 
        "etternavn": "Hausnes", 
        "hobby": ["Telemark", "Nerding", "Chips"] 
    },
    "ugga@bugga.com" : {
        "fornavn": "Ugga", 
        "etternavn": "Bugga", 
        "hobby": ["Ugging", "Bugging", "Uggingbugging"]
    }
}

# Iterer gjennom alle personene i personer og skriv ut fornavn og etternavn
for epost, info in personer.items():
    print(f"{info['fornavn']} {info['etternavn']} med epost {epost} har følgende hobbyer: {', '.join(info['hobby'])}")