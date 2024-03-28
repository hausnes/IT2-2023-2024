import pygame
import sys
import random

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player()
        self.font = pygame.font.Font(None, 36)  
        self.text = None
        self.text_time = 0

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.player.update()
        current_time = pygame.time.get_ticks()
        if current_time - self.text_time > 2000: # 2 sek.
            self.text = self.font.render("Pop, pop, pop! :)", True, (255, 255, 255))
            self.text_pos = (random.randint(100, 300), random.randint(100, 300))
            self.text_time = current_time
        elif current_time - self.text_time > 500:  # 0.5 sek.
            self.text = None

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.player.draw(self.screen)
        if self.text:
            self.screen.blit(self.text, self.text_pos)

class Player:
    def __init__(self):
        self.x = 250
        self.y = 250
        self.speed = 5

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        radius = 25  
        if keys[pygame.K_LEFT] and self.x - self.speed - radius > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x + self.speed + radius < 500:
            self.x += self.speed
        if keys[pygame.K_UP] and self.y - self.speed - radius > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y + self.speed + radius < 500:
            self.y += self.speed

    def update(self):
        self.handle_keys()

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (self.x, self.y), 25)

if __name__ == "__main__":
    Game().run()