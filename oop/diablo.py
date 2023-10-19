import random

class Character:
    def __init__(self, name, level, hp, mana):
        self.name = name
        self.level = level
        self.hp = hp
        self.mana = mana

    def __str__(self):
        return f"Name: {self.name}, Level: {self.level}, HP: {self.hp}, Mana: {self.mana}"
    
    def get_name(self):
        return self.name
    
    def get_level(self):
        return self.level
    
    def get_hp(self):
        return self.hp
    
    def get_mana(self):
        return self.mana
    
    def set_name(self, new_name):
        self.name = new_name

    def set_level(self, new_level):
        self.level = new_level

    def set_hp(self, new_hp):
        self.hp = new_hp

    def set_mana(self, new_mana):
        self.mana = new_mana

    def is_alive(self):
        return self.hp > 0
    
    def hit(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def heal(self, amount):
        self.hp += amount
        if self.hp > 100:
            self.hp = 100

    def cast_spell(self, cost):
        self.mana -= cost
        if self.mana < 0:
            self.mana = 0

# Lagar helten
hero = Character("Jo Bjørnar den objektorienterte", 1, 100, 100)
print(f"All informasjon om helten: {hero}") # Skriv ut informasjon om helten, kallar __str__-metoden
# Lagar bossen
boss = Character("Lars den Rektorianske", 1, 100, 100)
print(f"All informasjon om bossen: {boss}") # Skriv ut informasjon om bossen, kallar __str__-metoden

# Gjer gjerne meir ut av delen over, der du kan sette meir avanserte verdier for helten og bossen
# Kanskje du til og med kan la spelaren setje verdiane sjølv for helten (tenk "character creation")?

# Kampen
while hero.is_alive() and boss.is_alive():
    # Helten sin tur
    angrip = input("Vil du angripe? (ja/nei) ")
    if angrip == "ja":
        print("Du angriper!")
        boss.hit(20) # Gjer gjerne denne delen random (tilfeldig skade)
        print(f"Bossen har {boss.get_hp()} HP igjen.")
    elif angrip == "nei":
        print("Du angriper ikkje, og healer derfor!")
        hero.heal(10) # Gjer gjerne denne delen random (tilfeldig heal)
    else:
        print("Du må skrive ja eller nei!")
        continue
    
    # Gjer det tilfeldig om bossen angrip, må ta seg ein pause, eller kanskje healer? Sistnemnte er ikkje implementert endå
    boss_angrip = random.choice([True, False])
    if boss_angrip:
        print("Bossen angriper!")
        hero.hit(10) # Gjer gjerne denne delen random (tilfeldig skade)
        print(f"Du har {hero.get_hp()} HP igjen.")

        print(f"Etter angrepet så har helten {hero.get_hp()} HP og bossen {boss.get_hp()} HP.")
    else:
        print(f"{boss.get_name()} klarar ikkje gjere noko. Han forstår ikkje OOP og må ta seg ein pause.")
    
    print()

# Skriv ut resultatet av kampen (sidan me er ferdige med while-løkka , dvs ein av dei er døde)
print()
print("Kampen er over!")
print(f"Etter kampen så har helten {hero.get_hp()} HP og bossen {boss.get_hp()} HP.")