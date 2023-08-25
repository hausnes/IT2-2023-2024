try:
    poengsumElev = int(input("Skriv inn poengsum: "))
    
    if  poengsumElev >= 100 or poengsumElev < 0:
        print("Ugyldig poengsum!")
    elif poengsumElev >= 91:
        karakter = 6
    elif poengsumElev >= 81:
        karakter = 5
    elif poengsumElev >= 61:
        karakter = 4
    elif poengsumElev >= 41:
        karakter = 3
    elif poengsumElev >= 21:
        karakter = 2
    else:
        karakter = 1

    print(f"Karakteren til eleven er {karakter}.")

except ValueError: # Hvis konverteringen mislykkast, gjer ein feilmelding
    print("Du må skrive inn eit tal.")

'''

poengsumElev = int(input("Skriv inn poengsum: "))
    
if  poengsumElev >= 100 or poengsumElev < 0:
    print("Ugyldig poengsum!")
elif poengsumElev >= 91:
    karakter = 6
elif poengsumElev >= 81:
    karakter = 5
elif poengsumElev >= 61:
    karakter = 4
elif poengsumElev >= 41:
    karakter = 3
elif poengsumElev >= 21:
    karakter = 2
else:
    karakter = 1

print(f"Karakteren til eleven er {karakter}.")
'''