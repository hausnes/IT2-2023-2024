import random

class Weapon:
    def __init__(self, name, base_damage, ammo):
        self.name = name
        self.base_damage = base_damage
        self.ammo = ammo

class Character:
    ACTIONS = ["Angrip med våpen", "Heal", "Bruk magi"]

    def __init__(self, name, health, attack, defense, magic, weapon):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.magic = magic
        self.weapon = weapon

    def __str__(self):
        return f"{self.name}: Health = {self.health}, Attack = {self.attack}, Defense = {self.defense}"

    def perform_action(self, action, enemy):
        if action not in self.ACTIONS:
            print("Invalid action")
            return

        match action:
            case "Angrip med våpen":
                if self.weapon.ammo > 0:
                    damage = self.attack + self.weapon.base_damage - enemy.defense
                    print(f"{self.name} attacked with {self.weapon.name} and dealt {damage} damage. {self.weapon.ammo} ammo left")
                    print(f"Spesifisert: {self.attack} (attack) + {self.weapon.base_damage} (base damage) - {enemy.defense} (defense)")
                    self.weapon.ammo -= 1
                else:
                    print("No ammo left")
                    return
            case "Heal":
                self.health += 10
                print(f"{self.name} healed for 10 health. {self.health} health left")
                return
            case "Bruk magi":
                damage = self.magic - enemy.defense
            case _:
                print("Invalid action")
                return

        enemy.health -= damage
        print(f"{self.name} performed {action} on {enemy.name} and dealt {damage} damage. {enemy.health} health left")

    def is_alive(self):
        return self.health > 0

# Create some weapons
sverd = Weapon("Sverd", 10, 100)
pistol = Weapon("Pistol", 20, 5)

# Create some characters
hero = Character("Jo Bjørnar", 100, 10, 5, 15, sverd)
enemy = Character("Fiende", 100, 10, 5, 0, pistol)

# print(hero)
# print(hero.ACTIONS)

# hero.perform_action("Angrip med våpen", enemy)
# print(enemy)

# hero.perform_action("Bruk magi", enemy)
# print(enemy)

# enemy.perform_action("Angrip med våpen", hero)
# print(hero)

while hero.is_alive() and enemy.is_alive():
    # Hero's turn
    action = input(f"\nWhat should {hero.name} do? {hero.ACTIONS}: ")
    hero.perform_action(action, enemy)

    # Check if enemy is still alive
    if not enemy.is_alive():
        print()
        print(f"{enemy.name} has been defeated! {hero.name} wins!")
        break

    # Enemy's turn
    print()
    action = random.choice(enemy.ACTIONS)  # Enemy chooses a random action
    enemy.perform_action(action, hero)

    # Check if hero is still alive
    if not hero.is_alive():
        print()
        print(f"{hero.name} has been defeated! {enemy.name} wins!")
        break