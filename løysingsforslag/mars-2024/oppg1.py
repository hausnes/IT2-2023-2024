'''
Løysingsforslag med arv

'''

import pygame
import sys
import random
import time
import math

class Entity:
    ''' Ein super-klasse for både Player og Enemy. '''
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def draw(self, screen, color, size):
        pygame.draw.circle(screen, color, (self.x, self.y), size)

    def move(self, target):
        if self.x < target.x:
            self.x += self.speed
        elif self.x > target.x:
            self.x -= self.speed

        if self.y < target.y:
            self.y += self.speed
        elif self.y > target.y:
            self.y -= self.speed

class Player(Entity):
    ''' Ein sub-klasse av Entity, som legg til m.a. eigen move-funksjon, 
        og ei moglegheit for å angripe. '''
    def __init__(self):
        super().__init__(300, 200, 5)
        self.attack_radius = 100
        self.has_attacked = False

    def draw(self, screen):
        super().draw(screen, (255, 255, 255), 15)

    def move(self, key):
        ''' NB: Denne funksjonen overskriv move-metoden frå superklassen Entity 
            (..samanlikn med Enemy). '''
        if key[pygame.K_w]:
            self.y -= self.speed
        if key[pygame.K_s]:
            self.y += self.speed
        if key[pygame.K_a]:
            self.x -= self.speed
        if key[pygame.K_d]:
            self.x += self.speed

    def attack(self, enemies):
        if not self.has_attacked:
            # Opprettar ei tom liste for å lagre fiendar som er utanfor angrepsradiusen
            outside_attack_radius = []

            # Gå gjennom kvar fiende i lista med fiendar
            for enemy in enemies:
                # Berekn avstanden mellom fienden og spelaren
                distance = math.hypot(enemy.x - self.x, enemy.y - self.y)
                
                # Dersom avstanden er større enn angrepsradiusen, legg fienden til i den nye lista
                if distance > self.attack_radius:
                    outside_attack_radius.append(enemy)

            # Alternativt kan ein bruke list comprehension for å oppnå det same som i linjene overd
            #enemies[:] = [enemy for enemy in enemies if math.hypot(enemy.x - self.x, enemy.y - self.y) > self.attack_radius]

            # Tøm den gamle lista med fiender
            enemies.clear()

            # Legg til fiendene som er utenfor angrepsradiusen tilbake til enemies-lista
            enemies.extend(outside_attack_radius)

            # Dersom me hadde gjort det som i linja under, så hadde me berre oppretta ein ny
            # referanse til lista, medan den originale lista enemies i main-funksjonen ikkje blei endra.
            #enemies = outside_attack_radius
            
            self.has_attacked = True # Denne linja gjer at ein berre kan angripe ein gong, slå av og på etter behov

class Enemy(Entity):
    ''' Ein sub-klasse av Entity, som i dette tilfellet ikkje legg til særleg mykje.. merk likevel størrelse. '''
    def __init__(self):
        super().__init__(random.randint(0, 600), random.randint(0, 400), random.randint(1, 3))
        self.size = random.randint(10, 50)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.size)

'''
Game-loopen
'''
def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    clock = pygame.time.Clock()

    player = Player() # Opprettar spelar
    enemies = [] # Lagar ei liste som skal/kan innehalde ulike Enemy-instansar
    enemies.append(Enemy()) # Ved oppstart legg me ved ein Enemy-instans
    spawn_time = time.time() # Set ei starttid slik at me kan sjå kor lang tid er gått

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            player.attack(enemies)

        if time.time() - spawn_time > 10: # 10 som i at etter 10 sekunder så opprettast ein ny fiende
            enemies.append(Enemy())
            spawn_time = time.time() # Oppdaterer spawn_time slik at ein kan kan telle tida sidan sist fiende blei oppretta

        screen.fill((0, 0, 0))

        for enemy in enemies:
            enemy.move(player) # Hugs, player har x og y som enemy flyttar seg mot
            enemy.draw(screen)
            if pygame.Rect(player.x, player.y, 15, 15).colliderect(pygame.Rect(enemy.x, enemy.y, enemy.size, enemy.size)):
                pygame.quit()
                sys.exit()

        player.move(keys)
        player.draw(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()