# --------------------------------
# Oppgåve 6.1 frå oppgåvesamlinga
# --------------------------------

def er_palindrom(streng):
    # Fjerner alle mellomrom fra strengen og gjør den til små bokstaver
    streng = streng.replace(" ", "").lower()
    # Sjekker om strengen er lik seg selv baklengs ved å bruke slicing
    if streng == streng[::-1]: # Alternativ 1
        return True
    # if streng == ''.join(reversed(streng)): # Alternativ 2
    #     return True
    else:
        return False

# Tester funksjonen med noen eksempler
print(er_palindrom("anna")) # Skal skrive ut True
print(er_palindrom("ola")) # Skal skrive ut False
print(er_palindrom("agnes i senga")) # Skal skrive ut True
print(er_palindrom("python")) # Skal skrive ut False

print("annaB"[::-1])

# --------------------------------
# Oppgåve 6.2 frå oppgåvesamlinga
# --------------------------------

from imdb import Cinemagoer # https://cinemagoer.github.io/

# create an instance of the Cinemagoer class
ia = Cinemagoer()

# film = ia.search_movie("The Batman")
# print(film[0])
# print(film[0].movieID)
# film = ia.get_movie(film[0].movieID)
# print(film["runtime"])

# for key, value in film.items(): # NB: For å kunne sjå kva IMDB faktisk lagrar om filmane - dette er store mengder data, så det kan ta litt tid å skrive ut
#     print(f"Nøkkel: {key} \n Verdi: {value} \n\n")

def korrigere_data(data):
    # Lager en tom dictionary som skal inneholde de korrigerte dataene
    korrigert_data = {}
    # Går gjennom hvert element i den opprinnelige dictionary-en
    for film, tid in data.items():
        # Sjekker om tiden er 0 eller x, som er feil verdier
        print(f"Sjekkar filmen {film} med tida {tid}")
        if tid == 0 or tid == "x":
            # Hvis det er tilfellet, henter vi ut filmen fra imdb
            filmen = ia.search_movie(film)
            print("Fant filmen", filmen[0])
            filmen = ia.get_movie(filmen[0].movieID)
            # Henter ut riktig tid fra imdb
            tid = int(filmen["runtime"][0])
            print(f"Fant korrigert tid: {tid}")
        # Legger til filmen og den korrigerte tiden i den nye dictionary-en
        korrigert_data[film] = tid
    # Returnerer den korrigerte dictionary-en
    return korrigert_data

# Tester funksjonen med et eksempel
movie_runtimes = {
    "The Batman": 0, 
    "No Time To Die": 163, 
    "Dune": 155, 
    "Avengers: Endgame": 181, 
    "The Godfather": "177", 
    "The Lord of the Rings: The Return of the King": 201, 
    "Seven Samurai": 207, 
    "Gone With The Wind": 238, 
    "Lawrence of Arabia": 227, 
    "The Clock": 1440 
}

print("Korrigert data:")
print(korrigere_data(movie_runtimes))

# Leik med imdb
# get a movie
# movie = ia.get_movie('0133093')

# print the names of the directors of the movie
# print('Directors:')
# for director in movie['directors']:
#     print(director['name'])

# print the genres of the movie
# print('Genres:')
# for genre in movie['genres']:
#     print(genre)

# search for a person name
# people = ia.search_person('Mel Gibson')
# for person in people:
#    print(person.personID, person['name'])