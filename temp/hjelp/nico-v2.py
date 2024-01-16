import pygame
import sys

class Ball:
    def __init__(self, x, y, x_speed, y_speed, radius, color):
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.radius = radius
        self.color = color

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed

        if self.x - self.radius < 0 or self.x + self.radius > window_width:
            self.x_speed *= -1
        if self.y - self.radius < 0 or self.y + self.radius > window_height:
            self.y_speed *= -1

class Paddle:
    def __init__(self, x, y, width, height, color, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

    def draw(self, window):
        pygame.draw.rect(window, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def update(self, keys):
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

        if self.y < 0:
            self.y = 0
        if self.y > window_height - self.height:
            self.y = window_height - self.height

    '''
    def collide_with(self, ball): 
    This line defines the method. It takes two arguments: self, which is a 
    reference to the instance of the Paddle class that the method is being 
    called on, and ball, which is an instance of the Ball class.

    paddle_rect = pygame.Rect(self.x, self.y, self.width, self.height) 
    This line creates a pygame.Rect object for the paddle. A pygame.Rect 
    object represents a rectangle and is defined by its top-left corner 
    coordinates (self.x, self.y), its width (self.width), and its height (self.height).

    ball_rect = pygame.Rect(ball.x - ball.radius, ball.y - ball.radius, ball.radius * 2, ball.radius * 2) 
    This line creates a pygame.Rect object for the ball. Since the ball is represented 
    as a circle, the rectangle is created such that it circumscribes the circle. The 
    top-left corner of the rectangle is at (ball.x - ball.radius, ball.y - ball.radius), 
    and the width and height of the rectangle are both ball.radius * 2.

    return paddle_rect.colliderect(ball_rect) This line checks if the rectangle representing the paddle is colliding with the rectangle representing the ball. The colliderect method of a pygame.Rect object checks if it is colliding with another pygame.Rect object and returns True if they are colliding and False otherwise. The result of this check is returned by the collide_with method.
    '''
    def collide_with(self, ball):
        paddle_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        ball_rect = pygame.Rect(ball.x - ball.radius, ball.y - ball.radius, ball.radius * 2, ball.radius * 2)
        return paddle_rect.colliderect(ball_rect)

pygame.init()
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

ball = Ball(400, 300, 5, 5, 15, (255, 0, 0))
paddle = Paddle(50, 275, 15, 100, (0, 0, 255), 10)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    paddle.update(keys)

    if paddle.collide_with(ball):
        ball.x_speed *= -1  # reverse the ball's direction when it hits the paddle

    window.fill((255, 255, 255))
    ball.draw(window)
    ball.update()
    paddle.draw(window)

    pygame.display.flip()
    clock.tick(60)