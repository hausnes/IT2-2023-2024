# Wack-a-mole-ish game
# A game lasts for 10 seconds. A circle appears every 0.5 seconds. 
# If the player clicks on the circle, the score increases by 1. If the player misses the circle, the score remains the same. 
# At the end of the game, the score is printed to the console.

import pygame
import random
import time

class Circle:
    def __init__(self, screen):
        self.screen = screen
        self.x = random.randint(50, screen.get_width() - 50)
        self.y = random.randint(50, screen.get_height() - 50)
        self.radius = random.randint(10, 50)
        self.color = (255, 0, 0)

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def is_clicked(self, pos):
        print(f"Clicked at {pos[0]}, {pos[1]}")
        return ((self.x - pos[0]) ** 2 + (self.y - pos[1]) ** 2) <= self.radius ** 2

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.circle = None
        self.font = pygame.font.Font(None, 36)

    def start(self):
        self.circle = Circle(self.screen)

    def draw_timer(self, start_time, total_time):
        elapsed_time = time.time() - start_time
        remaining_time = max(0, total_time - elapsed_time)
        timer_text = f"Time remaining: {remaining_time:.1f}"
        timer_surface = self.font.render(timer_text, True, (255, 255, 255))
        self.screen.blit(timer_surface, (10, 10))

    def draw(self):
        self.screen.fill((0, 0, 0))
        if self.circle:
            self.circle.draw()

    def handle_click(self, pos):
        if self.circle and self.circle.is_clicked(pos):
            self.score += 1
            self.circle = None

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    game = Game(screen)
    game.start()

    total_time = 10
    start_time = time.time()
    last_circle_time = start_time
    while time.time() - start_time < total_time:  # Game lasts for 10 seconds
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game.handle_click(pygame.mouse.get_pos())

        current_time = time.time() # Check if it's time to spawn a new circle
        if current_time - last_circle_time >= 0.5: # Spawn a new circle every x seconds (0.5 in this case)
            game.circle = Circle(screen) 
            last_circle_time = current_time 

        # game.update()
        game.draw()
        game.draw_timer(start_time, total_time)
        
        pygame.display.flip()
        clock.tick(60)

    print(f"Game Over! Your score is {game.score}")
    pygame.quit()

if __name__ == "__main__":
    main()