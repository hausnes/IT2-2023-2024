# Oppgave: Lag et enkelt "Skyt spillet" med Pygame

# Lag et vindu med dimensjoner 800x600 piksler.
# Lag en spillerfigur som kan beveges horisontalt ved hjelp av piltastene.
# Legg til fiender som faller nedover skjermen fra toppen.
# Spilleren skal kunne skyte prosjektiler oppover ved å trykke på mellomromstasten.
# Hvis spillerens prosjektil treffer en fiende, får spilleren poeng.
# Hvis en fiende når bunnen av skjermen uten å bli truffet, mister spilleren et liv.
# Legg til en poengteller og en livsteller i spillet.
# Spillet skal avslutte når spilleren ikke har flere liv igjen.

import pygame as pg
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)
import math as m
from random import randint

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu der vi skal "tegne" innholdet vårt
VINDU_BREDDE = 800
VINDU_HOYDE  = 600
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

class Karakter:
  """Klasse for å representere en ball"""
  def __init__(self, x, y, fart, radius, farge, vindusobjekt):
    """Konstruktør"""
    self.x = x
    self.y = y
    self.fart = fart
    self.radius = radius
    self.farge = farge
    self.vindusobjekt = vindusobjekt
  
  def tegn(self, vindu):
    """Metode for å tegne ballen"""
    #pg.draw.circle(self.vindusobjekt, self.farge, (self.x, self.y), self.radius) 
    img = pg.image.load("spaeship.png")
    img = pg.transform.scale(img,(100,100))
    vindu.blit(img, (self.x,self.y))

  def flytt(self, taster):
    """Metode for å flytte ballen"""
    if taster[K_LEFT]:
      self.x -= self.fart
    if taster[K_RIGHT]:
      self.x += self.fart




class Romvesen:
    def __init__(self, x, y, fart, radius, vindusobjekt):
        """Konstruktør"""
        self.x = x
        self.y = y
        self.fart = fart
        self.radius = radius
        self.vindusobjekt = vindusobjekt
  
    def tegn(self, vindu):
    
        #pg.draw.circle(self.vindusobjekt, self.farge, (self.x, self.y), self.radius) 
        img = pg.image.load("Romvesen.png")
        img = pg.transform.scale(img,(100,100))
        vindu.blit(img, (self.x,self.y))

       

    def flytt(self):
        """Metode for å flytte ballen"""
        # Sjekker om ballen er utenfor høyre/venstre kant
        if ((self.x - self.radius) <= 0) or ((self.x + self.radius) >= self.vindusobjekt.get_width()):
          self.fart = self.fart
    
        # Flytter ballen
        self.x += self.fart


class projectile:
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        pg.draw.circle(win, self.color, (self.x,self.y), self.radius)



star_x = []
star_y = []

star2_x = []
star2_y = []
for i in range(50):
    star_x.append(randint(0,VINDU_BREDDE))
    star_y.append(randint(0,VINDU_HOYDE))
    
    star2_x.append(randint(0,VINDU_BREDDE))
    star2_y.append(randint(0,VINDU_HOYDE))



# Lager et Ball-objekt
karakter = Karakter(400, 475, 5, 20, (255, 69, 0), vindu)

romvesen = Romvesen(400, 70, 5, 20, vindu)

# Gjenta helt til brukeren lukker vinduet
fortsett = True
while fortsett:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False

    # Farger bakgrunnen lyseblå
    vindu.fill("black")

    for i in range(50):
        star_y[i] += 2
        star2_y[i] += 1
        if star_y[i] >= vindu.get_height():
            star_y[i] = 0
        if star2_y[i] >= vindu.get_height():
            star2_y[i] = 0
        pg.draw.rect(vindu,(255,255,255), pg.Rect(star_x[i],star_y[i], 5, 5,))
        pg.draw.rect(vindu,(255,255,255), pg.Rect(star2_x[i],star2_y[i], 2, 2,))
    
    # Henter en ordbok med status for alle tastatur-taster
    trykkede_taster = pg.key.get_pressed()


    # Tegner og flytter ballene
    karakter.tegn(vindu)
    karakter.flytt(trykkede_taster)
    romvesen.tegn(vindu)
    romvesen.flytt()

    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()