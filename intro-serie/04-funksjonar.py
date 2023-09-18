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