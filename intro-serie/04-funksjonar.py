import random

navn = input('Kva heiter du? ')

# Definerer ein funksjon som genererer tilfeldige høglege helsingar
def tilfeldigHelsing(navn):
    # Definerer ei liste med helsingar
    helsingar = ['Hei', 'Hallo', 'God dag', 'God kveld', 'God natt', 'Heisann', 'Hei på deg', 'Hallaisen', 'Hallois', 'Heisann hoppsann']
    # Returnerer ei tilfeldig helsing frå lista
    return random.choice(helsingar) + ", " + navn

# print(f'{tilfeldigHelsing()} {navn}!')
print(tilfeldigHelsing(navn))

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

# Define a function that takes a letter as an argument
def is_vowel(letter):
    # Convert the letter to lowercase
    letter = letter.lower()
    # Check if the letter is in the set of vowels
    if letter in {"a", "e", "i", "o", "u"}:
        # Return True if it is a vowel
        return True
    else:
        # Return False otherwise
        return False

# Test the function with some examples
print(is_vowel("A")) # True
print(is_vowel("b")) # False
print(is_vowel("E")) # True
print(is_vowel("f")) # False

# Define a function that takes minutes as an argument
# Define a dictionary with movie titles as keys and runtimes as values
movie_runtimes = {
    "The Batman": 180, 
    "No Time To Die": 163, 
    "Dune": 155, 
    "Avengers: Endgame": 181, 
    "The Godfather": 177, 
    "The Lord of the Rings: The Return of the King": 201, 
    "Seven Samurai": 207, 
    "Gone With The Wind": 238, 
    "Lawrence of Arabia": 227, 
    "The Clock": 1440 
}

def minutes_to_hours_and_minutes(minutes):
    # Check if the minutes are valid
    if minutes < 0:
        # Return an error message if not
        return "Invalid input: minutes cannot be negative"
    else:
        # Calculate the hours and minutes using integer division and modulo
        hours = minutes // 60
        minutes = minutes % 60
        # Return a formatted string with the hours and minutes
        return f"{hours} hour(s) and {minutes} minute(s)"

# Test the function with some examples
print(minutes_to_hours_and_minutes(90)) # 1 hour(s) and 30 minute(s)
print(minutes_to_hours_and_minutes(0)) # 0 hour(s) and 0 minute(s)
print(minutes_to_hours_and_minutes(-10)) # Invalid input: minutes cannot be negative

for movie in movie_runtimes:
    # Get the runtime of the current movie
    runtime = movie_runtimes[movie]
    # Convert the runtime to hours and minutes
    runtime = minutes_to_hours_and_minutes(runtime)
    # Print the movie and its runtime
    print(f"{movie} has a runtime of {runtime}")

# Ein funksjon som reknar ut potensiell energi - eksempel på å ha valfrie parameter
def potensiellEnergi(m, h, g=9.81):
    print(f"En gjenstand med massen {m} kg ved høyden {h} m har den potensielle energien {m*g*h:.2f} J (med g = {g})." )

potensiellEnergi(50, 10)
potensiellEnergi(50, 10, g=1.62)
potensiellEnergi(50, 10, 1.62)

# Definerer ein funksjon som tel antall ord i ein tekst
def antallOrd(tekst):
    # Returnerer lengda til lista med ord i teksten
    return len(tekst.split())

tekst = "Hei på deg!"

print(f"Antalet ord i '{tekst}' er {antallOrd(tekst)}")

# Definerer ein funksjon som tar inn en liste som parameter og returnerer en liste med de doblede verdiene
def dobleListe(liste):
    # Oppretter en tom liste som skal inneholde de doblede verdiene
    doblet = []
    # Går gjennom hvert element i den opprinnelige listen
    for tall in liste:
        # Dobler elementet og legger det til den nye listen
        doblet.append(tall * 2)
    # Returnerer den nye listen
    return doblet

# Lager en liste med noen tall
minListe = [1, 2, 3, 4, 5]
# Kaller på funksjonen med listen som parameter
minDobledeListe = dobleListe(minListe)
# Skriver ut den opprinnelige og den doblede listen
print("Opprinnelig liste:", minListe)
print("Doblet liste:", minDobledeListe)

# Eksempel på ein rekuriv funksjon
def rekursiv_sum(n):
    if n <= 1:
        return n
    else:
        return n + rekursiv_sum(n-1)

print(rekursiv_sum(10))

# Eksempel på korleis me kan be om forklaring/hjelp til ein funksjon
help(random.randint) # NB: Me har importert random-biblioteket heilt øvst i koden

# Eksempel på korleis me kan skrive ein funksjon som me dokumenterer
def terning(antallSider: int) -> int:
    """Returnerer et tilfeldig heltall i intervallet [1, antallSider], med begge endepunktente inkludert."""
    return random.randint(1, antallSider)

print(terning(6))
help(terning)