# A simple Pong game, using pygame and OOP

import pygame
import sys

class Paddle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def move(self, speed):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-speed, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(speed, 0)

    def draw(self, screen):
        pygame.draw.rect(screen, pygame.Color('white'), self.rect)

class Ball:
    def __init__(self, x, y, width, height, speed, screen_width, screen_height):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed
        self.dx = 1  # direction of movement in x axis
        self.dy = 1  # direction of movement in y axis
        self.screen_width = screen_width
        self.screen_height = screen_height

    def move(self):
        self.rect.move_ip(self.speed * self.dx, self.speed * self.dy)
        if self.rect.left < 0 or self.rect.right > self.screen_width:
            self.dx *= -1  # reverse direction
        if self.rect.top < 0 or self.rect.bottom > self.screen_height:
            self.dy *= -1  # reverse direction

    def draw(self, screen):
        pygame.draw.rect(screen, pygame.Color('white'), self.rect)

class Pong:
    def __init__(self, screen_width, screen_height):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.paddle = Paddle(screen_width // 2, screen_height - 20, 60, 10)
        self.ball = Ball(screen_width // 2, screen_height // 2, 10, 10, 2, screen_width, screen_height)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(pygame.Color('black'))
            self.paddle.move(10)
            self.ball.move()
            if self.paddle.rect.colliderect(self.ball.rect):
                self.ball.dy *= -1

            self.paddle.draw(self.screen)
            self.ball.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    Pong(640, 480).run()