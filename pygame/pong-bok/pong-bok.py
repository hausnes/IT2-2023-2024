import pygame as pg
import math as m

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 800
VINDU_HOYDE  = 600
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

class Ball:
  """Klasse for å representere en ball"""
  def __init__(self, x, y, x_fart, y_fart, radius, vindusobjekt):
    """Konstruktør"""
    self.x = x
    self.y = y
    self.x_fart = x_fart
    self.y_fart = y_fart
    self.radius = radius
    self.vindusobjekt = vindusobjekt
  
  def tegn(self):
    """Metode for å tegne ballen"""
    pg.draw.circle(self.vindusobjekt, (255, 69, 0), (self.x, self.y), self.radius) 

  def flytt(self):
    """Metode for å flytte ballen"""
    # Sjekker om ballen er utenfor høyre/venstre kant
    if ((self.x - self.radius) <= 0) or ((self.x + self.radius) >= self.vindusobjekt.get_width()):
      self.x_fart = -self.x_fart

    # Sjekker om ballen er utenfor toppen/bunnen
    if ((self.y - self.radius) <= 0) or ((self.y + self.radius) >= self.vindusobjekt.get_height()):
      self.y_fart = -self.y_fart
       
    # Flytter ballen
    self.x += self.x_fart
    self.y += self.y_fart

def finnAvstand(obj1, obj2):
    xAvstand2 = (obj1.x - obj2.x)**2  # x-avstand i andre
    yAvstand2 = (obj1.y - obj2.y)**2  # y-avstand i andre
    avstand = m.sqrt(xAvstand2 + yAvstand2)

    return avstand
    
# Lager et Ball-objekt
ball = Ball(225, 100, 0.1, 0.1, 10, vindu)
# Lager et annet Ball-objekt
ball2 = Ball(400, 300, 0.2, 0.2, 15, vindu)

# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    # Farger bakgrunnen lyseblå
    vindu.fill((135, 206, 235))

    # Tegner og flytter ballen
    ball.tegn()
    ball.flytt()
    ball2.tegn()
    ball2.flytt()

    # Sjekker om ballene treffer hverandre
    if finnAvstand(ball, ball2) <= (ball.radius + ball2.radius):
        print("Ballene treffer hverandre!")
        ball.x_fart = 0
        ball.y_fart = 0
        ball2.x_fart = 0
        ball2.y_fart = 0

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()