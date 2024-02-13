# Ein funksjon som reknar ut potensiell energi - eksempel på å ha valfrie parameter
def potensiellEnergi(m=20, h=2, g=9.81):
    print(f"En gjenstand med massen {m} kg ved høyden {h} m har den potensielle energien {m*g*h:.2f} J (med g = {g})." )

potensiellEnergi(50, 10)
potensiellEnergi(50, 10, g=1.62)
potensiellEnergi(50, 10, 1.62)