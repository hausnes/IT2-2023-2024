# Gjett tallet! Programmet under er et program som lagrer et hemmelig tall mellom 1-100 i en variabel og spør brukeren om å gjette tallet. 
# Det som mangler i programmet er betingelsen(e) for å gi beskjed om tallet som ble gjettet var for høyt eller for lavt. 
# Hvis brukeren gjetter feil skal han/hun få beskjed om å prøve på nytt. Skriv den manglende koden slik at programmet fungerer.

import random

hemmeligTall = random.randint(0,100) # Hent et tilfeldig tall

gjettet = 0 # Initier variabelen for gjettet tall
antGjett = 0 # Initier counter for antall forsøk

while gjettet != hemmeligTall:
    
    gjettet = int(input('Gjett det hemmelige tallet (1-100): ')) # Ta inn et gjett fra bruker
    antGjett += 1 # Øk antall forsøk med 1 for hver runde
    
    ### Skriv din kode under denne linjen ###
    if gjettet>hemmeligTall:
        print('Du gjetta for høgt. Forsøk igjen.')
    else:
        print('Du gjetta for lågt. Forsøk igjen.')
    
    ### Skriv din kode over denne linjen ###

print('Du gjettet riktig! Det hemmelige tallet var', hemmeligTall, '. Du brukte', antGjett, 'forsøk.')