import pygame
import sys

class ImageObject:
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (100, 100))  # Scale the image
        self.rect = self.image.get_rect(center=(x, y))
        self.angle = 0

    def draw(self, window):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        new_rect = rotated_image.get_rect(center=self.rect.center)
        window.blit(rotated_image, new_rect.topleft)

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.angle += 5
        if keys[pygame.K_RIGHT]:
            self.angle -= 5

def main():
    pygame.init()
    window = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    image_object = ImageObject(400, 300, 'spaceship.png')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        image_object.update(keys)

        window.fill((255, 255, 255))
        image_object.draw(window)

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()