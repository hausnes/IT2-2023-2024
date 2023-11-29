import pygame as pg
from pygame.locals import *

WIDTH, HEIGHT = 400, 600   # lenge og bredden av skjermen
FPS = 96  # Frame per second. 

class Skutt(pg.sprite.Sprite):
    def __init__(self,x,y) -> None:
        super().__init__()
        self.image = pg.Surface((10, 10))
        self.rect = self.image.get_rect()
        self.y_fart = 1
        self.farge = "red"
        pg.draw.line(self.image,"red",(5,0),(5,10),4)
        self.rect.x = x
        self.rect.y = HEIGHT-(HEIGHT-self.rect.height)/4
        self.image.set_colorkey("black")

    def update(self):
        # Flytter hinderet
        self.rect.y -= self.y_fart

class Fly(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((50, 50))
        self.rect = self.image.get_rect()
        pg.draw.circle(self.image, "yellow", (25, 25), 25)
        pg.draw.circle(self.image, "red", (25,25), 25, 5)
        self.rect.x = (WIDTH-self.rect.width)/2
        self.rect.y = HEIGHT-(HEIGHT-self.rect.height)/4
        self.fart_x = 1
        self.fart_y = 1
        

    def update(self):
      keys = pg.key.get_pressed()
      if keys[pg.K_LEFT] and self.rect.left > 0:
         self.rect.x -= self.fart_x
      if keys[pg.K_RIGHT] and self.rect.right < WIDTH:
         self.rect.x += self.fart_x
      
class App:
    def __init__(self):
        pg.init()  #Pygame blir initialisert
        self.clock = pg.time.Clock() #Den klokken trenger jeg for FPS
        self.screen = pg.display.set_mode((WIDTH, HEIGHT)) # pygame lager en skjerm. 
        pg.display.set_caption("pygame mal") #Navn i headeren av vinduet
        self.running = True #Hvis true da kjører programmet. 
        self.all_sprites = pg.sprite.Group() #Har ligger alle bilder tegninger inn. sprite.group har funksjoner for kolisjon og tegning osv. 
        self.fly = Fly()
        self.all_sprites.add(self.fly)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT: #hvis vi trykker på x øverst i vinduet da sluter programmet og animasjonen
                self.running = False #nå sluter dern 

            if event.type==pg.KEYDOWN:
               if event.key == pg.K_SPACE:
                  bullet = Skutt(self.fly.rect.x+self.fly.rect.width/2 -5,self.fly.rect.y-10)
                  self.all_sprites.add(bullet)   

    def update(self):
        self.all_sprites.update()  #viser alle tegninger bilder osv på skjermen, på sin riktige posisjon. 

    def draw(self):
        self.screen.fill("black")
        self.all_sprites.draw(self.screen) #tegner alle objekter men den er da ikke på skjermen ennå
        pg.display.update() #nå kommer den på skjermen. 

    def run(self):
        print((self.all_sprites.spritedict))
        while self.running: #så lenge den er True
            self.handle_events()   # ser på x in vinduet men kan også se taster kolisjon osv
            self.update() #viser det riktige på skjermen. 
            self.draw() # tegner på skjermen, men viser det nye ikke
            self.clock.tick(FPS) #klokken som tikker i 24 FPS
            
        pg.quit() # self.running er nå False. 

if __name__ == "__main__": # Hvis jeg kjører den filen da blir den funksjonen brukt, hvis jeg arver av den da blir den ikke brukt. 
    app = App()
    app.run()