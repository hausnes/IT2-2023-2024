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
    
    def volum(self):
        """Metode for å beregne volum"""
        return 4/3 * 3.14 * self.radius ** 3
    
    def __str__(self):
        """Metode for å skrive ut informasjon om en planet"""
        return f"Planeten {self.navn} har {self.antallRinger} ringer, er {self.solavstand} millioner km unna sola og har radius {self.radius} km. Arealet til {self.navn} er {self.areal():.2f} kvadratkilometer."

    def visInfo(self): # NB: Bruk heller __str__ -metoden
        """Metode for å skrive ut informasjon om en planet"""
        print(f"Planeten {self.navn} har {self.antallRinger} ringer, er {self.solavstand} millioner km unna sola og har radius {self.radius} km.")
        print(f"Arealet til {self.navn} er {self.areal():.2f} kvadratkilometer.")

    def leggTilMaane(self, maaneObjekt):
        """Metode for å legge til en måne"""
        self.maaner.append(maaneObjekt)

    def visMaaner(self):
        """Metode for å skrive ut informasjon om månene til en planet"""
        if len(self.maaner) == 0:
            print(f"{self.navn} har ingen måner.")
            return
        else:
            print(f"Månene til {self.navn} er:")
            for m in self.maaner:
                print(m)
                # beregne forholdet mellom hver månes volum og planetens volum. Dette forholdstallet skal skrives ut sammen med månenes navn. Hvis planeten ikke har noen måner, skal en passende beskjed skrives ut.
                print(f"Forholdet mellom volumet til {m.navn} og {self.navn} er {m.volum() / self.volum():.2f}")


class Maane:
    '''Klasse for å representere en måne'''
    def __init__(self, navn, radius = 0):
        '''Konstruktør'''
        self.navn = navn
        self.radius = radius

    def __str__(self):
        '''Metode for å skrive ut informasjon om en måne'''
        return f'Månen {self.navn} har radius {self.radius} km.'
    
    def volum(self):
        '''Metode for å beregne volum'''
        return 4/3 * 3.14 * self.radius ** 3
    
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
    # print(p.visInfo())
    print(p) # NB: Denne bruker automatisk __str__ -metoden

# Kan legge til måner (men merk at dette bør gjerast vha. ein eigen klasse for måner etterkvart)
# planeter["Jupiter"].leggTilMaane("Io")
# planeter["Jupiter"].leggTilMaane("Europa")
# planeter["Jupiter"].leggTilMaane("Ganymedes")

# Lager måne-objekter
io = Maane("Io", 1821.6)
europa = Maane("Europa", 1560.8)
ganymedes = Maane("Ganymedes", 2634.1)

# Legger til måne-objekter
planeter["Jupiter"].leggTilMaane(io)
planeter["Jupiter"].leggTilMaane(europa)
planeter["Jupiter"].leggTilMaane(ganymedes)

# Kan printe ut månene til Jupiter
# print(f"Månene til Jupiter er {planeter['Jupiter'].maaner}")
planeter["Jupiter"].visMaaner()
planeter["Mars"].visMaaner()