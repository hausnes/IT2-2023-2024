import random

navn = input('Kva heiter du? ')

# Definerer ein funksjon som genererer tilfeldige høglege helsingar
def tilfeldigHelsing():
    # Definerer ei liste med helsingar
    helsingar = ['Hei', 'Hallo', 'God dag', 'God kveld', 'God natt', 'Heisann', 'Hei på deg', 'Hallaisen', 'Hallois', 'Heisann hoppsann']
    # Returnerer ei tilfeldig helsing frå lista
    return random.choice(helsingar)

print(f'{tilfeldigHelsing()} {navn}!')

# Definerer ein funksjon som tek inn to parametere: navn og språk
def hels(navn, spraak):
    # Sjekkar språket og skriv ut ei helsing på det språket
    if spraak == "Engelsk":
        print(f"Hello, {navn}!")
    elif spraak == "Fransk":
        print(f"Bonjour, {navn}!")
    elif spraak == "Spansk":
        print(f"Hola, {navn}!")
    else:
        print(f"Orsak, eg har ikkje lært meg {spraak} endå.")

# Eksempel på korleis funksjonen kan brukast
hels(navn, "Engelsk")
hels(navn, "Fransk")
hels(navn, "Spansk")
hels(navn, "Tysk")