class Planet:
    def __init__(self, navn, solavstand, radius):
        self.navn = navn
        self.solavstand = solavstand
        self.radius = radius

mars = Planet("Mars", 227.9, 3389.5)
jupiter = Planet("Jupiter", 778.5, 69911)

uranus = Planet("Uranus", 150, 10000000000)

jupiter.radius = 20000 # Endre radiusen til Jupiter
print(jupiter.radius)

# Kan printe ut kva datatype det er
print(type(mars))
