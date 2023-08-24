try:
    operasjon = input("Skriv inn en operasjon (+, -, *, /): ")
    a = float(input("Skriv inn et tall: "))
    b = float(input("Skriv inn et tall: "))
    resultat = 0

    def pluss(a, b):
        return a + b

    def minus(a, b):
        return a - b

    def gange(a, b):
        return a * b

    def dele(a, b):
        return a / b

    # Lager en ordbok som mapper en operasjon til en funksjon
    funksjoner = {
        "+": pluss,
        "-": minus,
        "*": gange,
        "/": dele
    }

    # Henter funksjonen som tilsvarer operasjonen fra ordboken
    funksjon = funksjoner.get(operasjon)

    # Sjekker om funksjonen finnes
    if funksjon:
        # Kaller funksjonen med argumentene a og b
        resultat = funksjon(a, b)
        print(f"Resultatet av {a} {operasjon} {b} er {resultat}")
    else:
        print("Ugyldig operasjon")
except ValueError:
    print("Du må skrive inn et tall.")