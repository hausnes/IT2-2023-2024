gyldig = False

while not gyldig:
    tall = input("Skriv et tall: ")

    try:
        tall = int(tall)
        gyldig = True
    except ValueError:
        print("Du må skrive inn et heltall.")

print(f"Du skrev inn {tall}.")