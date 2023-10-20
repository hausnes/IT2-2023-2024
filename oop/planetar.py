class Planet:
    """Klasse for å representere en planet"""
    def __init__(self, navn, solavstand, radius, antallRinger = 0):
        """Konstruktør"""
        self.navn = navn
        self.solavstand = solavstand
        self.radius = radius
        self.antallRinger = antallRinger
        self.maaner = [] # Liste som skal holde på måner

    def areal(self):
        """Metode for å beregne areal"""
        return 4 * 3.14 * self.radius ** 2
    
    def visInfo(self):
        """Metode for å skrive ut informasjon om en planet"""
        print(f"Planeten {self.navn} har {self.antallRinger} ringer, er {self.solavstand} millioner km unna sola og har radius {self.radius} km.")
        print(f"Arealet til {self.navn} er {self.areal():.2f} kvadratkilometer.")

    def leggTilMaane(self, maane):
        """Metode for å legge til en måne"""
        self.maaner.append(maane)

# Lager en ordbok som holder på Planet-objekter
planeter = {}

# Lager og legger til noen Planet-objekter
planeter["Mars"] = Planet("Mars", 227.9, 3389.5)
planeter["Jupiter"] = Planet("Jupiter", 778.5, 20000, 4)
planeter["Saturn"] = Planet("Saturn", 1434000, 58232, 7)

# Endre radiusen til Jupiter
planeter["Jupiter"].radius = 69911 
print(f"Ny radius til Jupiter er {planeter['Jupiter'].radius}")

# Kan printe ut kva datatype det er
print(type(planeter["Mars"]))

# Kan printe ut informasjon om planetene
for p in planeter.values():
    print(p.visInfo())

# Kan legge til måner (men merk at dette bør gjerast vha. ein eigen klasse for måner etterkvart)
planeter["Jupiter"].leggTilMaane("Io")
planeter["Jupiter"].leggTilMaane("Europa")
planeter["Jupiter"].leggTilMaane("Ganymedes")

# Kan printe ut månene til Jupiter
print(f"Månene til Jupiter er {planeter['Jupiter'].maaner}")

liste = [1,2,3]
print(liste[0])