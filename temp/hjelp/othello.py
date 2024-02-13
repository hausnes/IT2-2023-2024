import pygame as pg

pg.init

x = "svart"
o = "hvit"
i = "ingenting"

bitmap = [
i,i,i,i,i,i,i,i,
i,i,i,i,i,i,i,i,
i,i,i,i,i,i,i,i,
i,i,i,i,i,i,i,i,
i,i,i,i,i,i,i,i,
i,i,i,i,i,i,i,i,
i,i,i,i,i,i,i,i,
i,i,i,i,i,i,i,i
]

koordinater = []*64


skjermHøyde = 800
skjermBredde = 800
skjerm = pg.display.set_mode([skjermBredde, skjermHøyde])

def tegnRuter(skjerm, bredde, høyde, liste):
    pixelhøyde = høyde/8
    pixelbredde = bredde/8
    pixelhøyde = int(pixelhøyde)
    pixelbredde = int(pixelbredde)
    xcor = 0
    ycor = 0
    i = 0
    for ycor in range(0, høyde + pixelhøyde, pixelhøyde):
        ycor -= pixelhøyde
        i+=1
        for xcor in range(0, bredde, pixelbredde):
            i+=1
            if xcor == bredde:
                xcor = 0
            if  i%2 == 0:
                pg.draw.rect(skjerm, (36, 135, 89), (xcor, ycor, pixelbredde, pixelhøyde), 0, 3)
                liste.append(((xcor + pixelbredde/2), (ycor + pixelhøyde/2)))
            else:
                pg.draw.rect(skjerm, (36, 158, 89), (xcor, ycor, pixelbredde, pixelhøyde), 0, 3)
                liste.append(((xcor + pixelbredde/2), (ycor + pixelhøyde/2)))
                #trenger midten av rutene i en liste

            print(liste,"\n", len(liste))

class Spiller():
    def __init__(self, score, farge, symbol):
        self.farge = farge
        self.score = score
        self.symbol = symbol

    def plasserBrikke(self, skjerm, liste, bitmap):
        mus = pg.mouse.get_pos()
        mus_trykket = pg.mouse.get_pressed()
        rutenummer = 0

        #finne rutenummer basert på positsjon
        for i in range(0, len(liste)):
            if -50 < mus[0] - liste[i][0] < 50 and -50 < mus[1] - liste[i][1] < 50:
                rutenummer = i


        if mus_trykket[0] == True and bitmap[rutenummer] == "ingenting":
            #plasser brikke på midten av ruten
            pg.draw.circle(skjerm, self.farge, liste[rutenummer], 40)
            bitmap[rutenummer] = self.symbol


spiller = Spiller(2, (255,255,255), o)
spiller2 = Spiller(2,(0,0,0), x)


kjør = True

while kjør:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            kjør = False
    #skriv
    
    tegnRuter(skjerm, skjermBredde, skjermHøyde, koordinater)
    # print(koordinater)
    spiller.plasserBrikke(skjerm, koordinater, bitmap)
    pg.display.flip()

pg.quit()