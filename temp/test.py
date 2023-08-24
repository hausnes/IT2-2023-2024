import calendar as cal
print(cal.month(1982, 5)) # Skriv ut kalender for mai 1982

tekst = "Hei"
print(tekst[-1:len(tekst)])

import math as m
print(m.pi)
print(f"PI er {m.pi:12.3f}")
print(f"PI er {m.pi:12.5f}")
print(f"PI er {m.pi:12.10f}")

navn = [
    "Øyvind",
    "Kari",
    "jo Bjørnar",
    "Ola",
    "Per"
]

for person in navn:
    print(f"Fornavn: {person:>12}")

print(navn[2].capitalize()) # Gjer første bokstav stor
print(navn[2].title()) # Gjer første bokstav i kvar ord stor

# Sykkeloppgåve
radius = 31.83 # meter
omkrets = 2 * m.pi * radius
lengde = 100 # meter
totalLengde = omkrets + lengde

fartSyklist = 50 # km/t
fartMeterPerSekund = fartSyklist / 3.6 # m/s

# Bereknar tida syklisten bruker på å sykle rundt sirkelen
tid = totalLengde / fartMeterPerSekund
print(f"Tida det tar å sykle rundt sirkelen er {tid:.2f} sekund.")

# Bereknar tida det tar å sykle rundt sirkelen 10 gonger
tid = tid * 10
print(f"Tida det tar å sykle rundt sirkelen 10 gonger er {tid:.2f} sekund.")

# Oppgåve frå boka om fjelltoppar
fjell = [ 
    ["Galdhøpiggen", 2469], 
    ["Glittertind", 2464], 
    ["Store Skagastølstind", 2405], 
    ["Store Styggedalstind", 2387], 
    ["Skarstind", 2373] 
]

print(fjell)

# Standard utskrift
for fjelltopp in fjell:
    print(f"{fjelltopp[0]} er {fjelltopp[1]} meter over havet.")

def forkort_navn(navn): # Bruker de tre første og de tre siste bokstavene i navnet
    return navn[:3] + "…" + navn[-3:]

# Utskrift med forkorting av navn, jfr. oppgåva
for fjelltopp in fjell:
    print(forkort_navn(fjelltopp[0]) + " er " + str(fjelltopp[1]) + " meter over havet.")