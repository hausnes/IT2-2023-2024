film_v1 = {
    "A Fish Called Wanda" : [130,170],
    "Lord of the Rings" : 223
}

print(film_v1["A Fish Called Wanda"])

film_v2 = {
    "A Fish Called Wanda" : {
        "runtime" : 130,
        "directors" : ["John Cleese", "Charles Cricton"],
        "rating" : 7.5
    },
    "A Fish Called Jo Bjørnar" : {
        "runtime" : 76,
        "directors" : ["Jo Bjørnar Hausnes", "Jobis"],
        "rating" : 10
    }
}

print(film_v2["A Fish Called Jo Bjørnar"]["directors"][1])

for utvalgtFilm in film_v2:
    film = film_v2[utvalgtFilm]
    print(film["rating"])

print("\nAlternativ framgangsmåte:")

for utvalgtFilm in film_v2:
    print(utvalgtFilm)
    print(film_v2[utvalgtFilm])
