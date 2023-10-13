class Planet:
    def __init__(self, navn, solavstand, radius):
        self.navn = navn
        self.solavstand = solavstand
        self.radius = radius

    def areal(self):
        return 4 * 3.14 * self.radius ** 2
    
    def formatertUtskrift(self):
        return f"Planet {self.navn} har solavstand {self.solavstand}, radius {self.radius} og areal {self.areal()}"

mars = Planet("Mars", 227.9, 3389.5)
jupiter = Planet("Jupiter", 778.5, 69911)

uranus = Planet("Uranus", 150, 10000000000)

jupiter.radius = 20000 # Endre radiusen til Jupiter
print(jupiter.radius)

# Kan printe ut kva datatype det er
print(type(mars))


for planet in [mars, jupiter, uranus]:
    print(planet.formatertUtskrift())