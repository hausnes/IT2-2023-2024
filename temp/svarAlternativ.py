svar = input("Hva står R for i RGB? ")

# Alternativ 1
if svar == "Rød" or svar == "rød" or svar == "red" or svar == "rED":
    print("Riktig.")

# # Alternativ 2
if svar.lower() == "rød" or svar.lower() == "red":
    print("Riktig.")

# Alternativ 3
if "rød" in svar.lower():
    print("Riktig!")