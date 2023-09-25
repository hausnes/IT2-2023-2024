## 
# Stein-saks-papir!
# 
# Skriv et program som tar inn et tilfeldig tall mellom 1-3 (1 = stein, 2 = saks, 3 = papir)  
# fra random-biblioteket, og enten stein('st'), saks('sa') eller papir('p') fra bruker. 
# Sammenlign valgene og sjekk hvem som vant ut fra følgende regler:
# Stein vs saks: stein vinner
# Stein vs papir: papir vinner
# Papir vs saks: saks vinner
# 
# Ved samme valg er det uavgjort.
#  
# Bruk if-elif-else for å skrive programmet. Skriv resultatet ut til konsoll.
#

## Svar
import random
valgMaskin = random.choice(["stein","saks","papir"])
valgBruker = input("Velg stein (st), saks (sa) eller papir (p): ")
if valgMaskin == valgBruker:
    print("Uavgjort")
elif valgMaskin == "stein" and valgBruker == "sa":
    print("Datamaskin vinner")
elif valgMaskin == "papir" and valgBruker == "st":
    print("Datamaskin vinner")
elif valgMaskin == "saks" and valgBruker == "p":
    print("Datamaskin vinner")
else:
    print("Du vant!")

print("Maskin valgte:",valgMaskin)

# Versjon 2: Nå skal du utvide programmet slik at den som vinner får 1 p. 
# Spill frem til spilleren eller datamaskinen har fått 10 p.
