fart = 0

def aukeFart():
    global fart
    fart = fart + 1
    print(f" Fart inne i: {fart}")

def senkeFart():
    global fart
    fart = fart - 1
    print(f" Fart inne i: {fart}")

aukeFart()
senkeFart()

print(f" Fart utanfor: {fart}")