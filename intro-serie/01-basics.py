# Variablar, datatypar og utskrift
fornavn = "Jo Bjørnar"
etternavn = "Hausnes"

print(fornavn, etternavn)

print(type(fornavn))

tallNrEin = 1
tallNrTo = 2.3

print(tallNrEin, tallNrTo)
print(type(tallNrEin))
print(type(tallNrTo))

print(tallNrEin + tallNrTo)

#print(fornavn + tallNrEin) # Dette fungerer ikkje, kvifor?
print(fornavn + str(tallNrEin)) # Dette fungerer, kvifor?

# Input frå brukar
# NB: input() returnerer alltid ein tekststreng
fornavn = input("Skriv inn fornavnet ditt: ")
print("Hei, " + fornavn)
alder = input("Skriv inn alderen din: ")
print("Du er " + alder + " år gammel")

# Konvertering av datatypar
alder = int(alder)

# Valgsetningar
if alder < 18:
    print("Du er under 18")
elif alder < 67:
    print("Du er i arbeidsfør alder")
else:
    print("Du er pensjonist")

# Lister
frukter = ["eple", "banan", "appelsin", "sitron"]
print(frukter)
print(frukter[0])

# Løkker
for frukt in frukter:
    print(frukt)

'''
Leik deg først med koden over (= endre, legg til, utforsk), og forsøk deretter å løyse oppgåvene under. Kopier oppgåveteksten inn i eigne filer.

Oppgave 1: Lag et program som ber brukeren om å skrive inn navnet sitt og fødselsåret sitt, og så skriver ut en hilsen som sier “Hei, [navn]! Du er [alder] år gammel.” For eksempel, hvis brukeren skriver inn “Ola” og “1982”, skal programmet skrive ut “Hei, Ola! Du er 42 år gammel.”

Oppgave 2: Lag et program som ber brukeren om å skrive inn et tall mellom 1 og 10, og så sjekker om tallet er likt, større eller mindre enn et tilfeldig valgt tall. Programmet skal skrive ut om brukeren gjettet riktig, for  høyt eller for lavt, og hva det tilfeldige tallet var. For å velge et tilfeldig tall, kan du bruke funksjonen random.randint(a, b) fra modulen random, som gir et heltall mellom a og b (inkludert). For eksempel, hvis brukeren skriver inn “5” og det tilfeldige tallet er “7”, skal programmet skrive ut “Du gjettet for lavt. Det tilfeldige tallet var 7.”

Oppgave 3: Lag et program som ber brukeren om å skrive inn navnet på en frukt, og så skriver ut om frukten er søt eller sur. Programmet skal ha en liste over søte frukter og en liste over sure frukter, og bruke valgsetninger til å sammenligne brukerens input med listene. Hvis frukten ikke finnes i noen av listene, skal programmet skrive ut at det ikke vet om frukten er søt eller sur. For eksempel, hvis brukeren skriver inn “eple”, skal programmet skrive ut “Eple er en søt frukt.” Hvis brukeren skriver inn “sitron”, skal programmet skrive ut “Sitron er en sur frukt.” Hvis brukeren skriver inn “banan”, skal programmet skrive ut “Jeg vet ikke om banan er søt eller sur.”
'''