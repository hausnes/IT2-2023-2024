# Eit program som skriv til og les frå ei fil, for å vise grunnleggande filhandtering i Python,
# samt konsepta med objektorientert programmering.

# NB: Legg merke til at du alltid legg til nye linjer i dokumentet, der dei gamle blir liggande (grunna append-modusen).

class Dokument:
    def __init__(self, filnavn):
        self.filnavn = filnavn

    def __str__(self):
        return f"{self.filnavn}"

    def skriv(self, tekst):
        with open(self.filnavn, 'a') as fil: # 'a' for append, legg til ny tekst i slutten av fila (= det gamle blir òg liggande)
            fil.write(tekst + '\n')

    def les(self):
        with open(self.filnavn, 'r') as fil:
            return fil.read()

    def les_linje(self, linje):
        with open(self.filnavn, 'r') as fil:
            return fil.readlines()[linje]

    def les_linjer(self, linjeFra, linjeTil):
        with open(self.filnavn, 'r') as fil:
            linjer = [linje.strip() for linje in fil.readlines()] # Fjerne linjeskiftet på slutten av linja
            return linjer[linjeFra:linjeTil]

# Oppretter objektet
dok = Dokument('utskrift.txt')

# Skriv ut filnamnet
print(dok)

# Skriv til dokumentet
dok.skriv('Dette er linje 1')
dok.skriv('Dette er linje 2')
dok.skriv('Dette er linje 3')
dok.skriv('Dette er linje 4')

# Leser heile dokumentet
print(f"Heile dokumentet:\n{dok.les()}")

# Leser ei linje i dokumentet
print(f"Den første linja i dokumentet: {dok.les_linje(0)}")

# Leser ei linje i dokumentet
print(f"Den tredje linja i dokumentet: {dok.les_linje(2)}") # Skrive om denne funksjonen slik at den blir meir logisk for ein "vanleg" brukar?

# Leser fleire linjer i dokumentet
print(f"Les fleire linjer frå dokumentet: {dok.les_linjer(0, 3)}")