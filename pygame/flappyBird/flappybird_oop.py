# To-do: Flytt kode frå flappybird til oop-versjon

import pygame, sys, random

class Bird:
    def __init__(self):
        self.surface = pygame.image.load("assets/bluebird.png").convert_alpha()
        self.rect = self.surface.get_rect(center=(50, 512 / 2))
        self.movement = 0

    def animate(self):
        # Add bird animation code here

    def rotate(self):
        # Add bird rotation code here

    def collision(self, pipes):
        for pipe in pipes:
            if self.rect.colliderect(pipe.rect):
                return False
        return True

class Pipe:
    def __init__(self):
        self.surface = pygame.image.load("assets/pipe-green.png")
        self.rect = self.create_pipe()

    def create_pipe(self):
        random_pipe_pos = random.choice([200, 250, 300, 350, 400])
        bottom_pipe = self.surface.get_rect(midtop=(500, random_pipe_pos))
        top_pipe = self.surface.get_rect(midtop=(500, random_pipe_pos - 450))
        return bottom_pipe, top_pipe

    def move(self):
        self.rect.centerx -= 5

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((288, 512))
        self.clock = pygame.time.Clock()
        self.game_active = True
        self.bird = Bird()
        self.pipes = []

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.movement = 0
                        self.bird.movement -= 5

                    if event.key == pygame.K_SPACE and self.game_active == False:
                        self.game_active = True
                        self.pipes.clear()
                        self.bird.rect.center = (50, 512 / 2)
                        self.bird.movement = 0

                if event.type == pygame.USEREVENT:
                    self.pipes.append(Pipe())

            if self.game_active:
                self.bird.movement += 0.25
                self.bird.rotate()
                self.bird.rect.centery += self.bird.movement
                self.screen.blit(self.bird.surface, self.bird.rect)
                self.game_active = self.bird.collision(self.pipes)

                for pipe in self.pipes:
                    pipe.move()
                    self.screen.blit(pipe.surface, pipe.rect)

            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    Game().run()