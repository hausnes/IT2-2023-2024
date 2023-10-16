class Rektangel:
    """Klasse for å representere et rektangel"""
    def __init__(self, lengde:int, bredde:int):
        """Konstruktør"""
        self.lengde = lengde
        self.bredde = bredde

    def areal(self):
        """Metode for å beregne areal"""
        return self.lengde * self.bredde

    def visInfo(self):
        """Skriver ut informasjon om et rektangel"""
        print(f"Rektangel med lengde {self.lengde} og bredde {self.bredde} har areal {self.areal()}")

class Kvadrat(Rektangel):
    """Klasse for å representere et kvadrat som er en spesialisering av rektangel (arver))"""
    def __init__(self, sidekant:int):
        super().__init__(sidekant, sidekant)

    def visInfo(self):
        """Skriver ut informasjon om et kvadrat"""
        print(f"Kvadrat med sidelengde {self.lengde} har areal {self.areal()}")

# Lager et kvadrat
k = Kvadrat(5)
k.visInfo()

# Liste som skal holde på rektangler
rektangler = []

# Lager og legger til noen rektangler
rektangler.append(Rektangel(2, 5))
rektangler.append(Rektangel(4, 3))
rektangler.append(Rektangel(5, 6))

for r in rektangler:
    r.visInfo()