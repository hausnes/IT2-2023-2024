import pygame
import random
import time

# Konstanter for skjermstørrelse
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class Game:
    def __init__(self):
        self.objects = []
        self.collision_sound = pygame.mixer.Sound('thump.wav')
        self.lives = 10

    def spawn_object(self):
        # Legg til et nytt fallende objekt på en tilfeldig x-posisjon
        x = random.randint(0, SCREEN_WIDTH)
        speed = random.randint(1, 5)
        self.objects.append(FallingObject(x, speed))

    def update(self):
        # Oppdater alle fallende objekter
        for obj in self.objects:
            obj.update()

            # Fjern objekter som har falt utenfor skjermen, og reduser antall liv
            if obj.y > SCREEN_HEIGHT:
                self.objects.remove(obj)
                self.lives -= 1
    
    def check_collisions(self, crosshair):
        for obj in self.objects:
            if crosshair.get_rect().colliderect(obj.get_rect()):
                # Spill av lyd ved kollisjon
                self.collision_sound.play()
                # Handle collision (e.g., remove object and increase score)
                self.objects.remove(obj)

class Crosshair:
    def __init__(self):
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2

    def draw(self, screen):
        # Tegn siktekrysset som et kryss
        pygame.draw.line(screen, (255, 255, 255), (self.x - 10, self.y), (self.x + 10, self.y), 2)
        pygame.draw.line(screen, (255, 255, 255), (self.x, self.y - 10), (self.x, self.y + 10), 2)
    
    def get_rect(self):
        return pygame.Rect(self.x - 10, self.y - 10, 20, 20)

class FallingObject:
    def __init__(self, x, speed):
        self.x = x
        self.y = 0
        self.speed = speed

    def update(self):
        # Flytt objektet nedover
        self.y += self.speed

    def draw(self, screen):
        # Tegn objektet som en firkant
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x - 10, self.y - 10, 20, 20))

    def get_rect(self):
        return pygame.Rect(self.x - 10, self.y - 10, 20, 20)

'''
Game loop
'''
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Lag ein font
font = pygame.font.Font(None, 36)

game = Game()
crosshair = Crosshair()

# For å kunne halde spelet i gang ein gitt periode
starttime = time.time()
runtime = 10

running = True

while running:
    # Avslutt spelet dersom det ikkje er fleire liv att
    if game.lives <= 0:
        running = False

    # Ser til at spelet avsluttar dersom tida er ute
    # print(time.time() - starttime)
    if (time.time() - starttime) > runtime:
        running = False

    # Avsluttar spelet dersom spelaren lukkar
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Oppdater siktekryssets posisjon til museposisjonen
    crosshair.x, crosshair.y = pygame.mouse.get_pos()

    # Spawne nye objekter med en viss sannsynlighet hver frame
    if random.random() < 0.02:
        game.spawn_object()

    game.update()

    game.check_collisions(crosshair)

    screen.fill((0, 0, 0))
    for obj in game.objects:
        obj.draw(screen)
    crosshair.draw(screen)

    # Tegn antall liv på skjermen
    lives_text = font.render(f"Lives: {game.lives}", True, (255, 255, 255))
    screen.blit(lives_text, (10, 10))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()