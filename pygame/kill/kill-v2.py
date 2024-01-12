import pygame
import sys
from pygame.sprite import Sprite, Group

class Ball(Sprite):
    def __init__(self, x, y, radius, screen, damping=0.9, player=False):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius
        self.screen = screen
        self.speed = 0
        self.damping = damping
        self.gravity = 0.1
        self.player = player
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)

    def update(self):
        if not self.player:
            self.speed += self.gravity
            self.y += self.speed

            if self.y + self.radius > self.screen.get_height():
                self.y = self.screen.get_height() - self.radius
                self.speed *= -self.damping

        self.rect.x = self.x - self.radius
        self.rect.y = self.y - self.radius

    def draw(self):
        pygame.draw.circle(self.screen, (255, 0, 0), (int(self.x), int(self.y)), self.radius)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    bouncing_ball = Ball(400, 0, 20, screen)
    bouncing_ball2 = Ball(200, 50, 20, screen)
    player_ball = Ball(500, screen.get_height() - 20, 20, screen, player=True)

    bouncing_balls = Group() # In Pygame, a `Group` is a container class for multiple `Sprite` objects. It provides several methods that make it easier to work with a collection of sprites. For example, you can call the `update` method on a `Group` to update all sprites in the group, or the `draw` method to draw all sprites in the group. In this case, you're using a `Group` for the bouncing balls to make it easier to check for collisions with the player ball. The `spritecollide` function can take a `Group` as an argument and will check for collisions between the given sprite and all sprites in the group. If you only have one bouncing ball, you technically don't need a `Group`. You could just check for a collision between the player ball and the bouncing ball directly. However, using a `Group` makes your code more flexible and easier to extend. If you want to add more bouncing balls in the future, you can simply add them to the `Group` and the collision detection code will still work.
    bouncing_balls.add(bouncing_ball)
    bouncing_balls.add(bouncing_ball2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_ball.x -= 5
        if keys[pygame.K_RIGHT]:
            player_ball.x += 5

        screen.fill((0, 0, 0))
        for ball in bouncing_balls:
            ball.update()
            ball.draw()
        player_ball.update()
        player_ball.draw()

        if pygame.sprite.spritecollide(player_ball, bouncing_balls, True): # True means that the bouncing ball will be removed from the group if there is a collision (i.e. "kill")
            print("Game Over!")
            # pygame.quit()
            # sys.exit()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()