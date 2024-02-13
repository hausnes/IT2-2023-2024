import pygame as pg

pg.init()

x = "svart"
o = "hvit"
i = "ingenting"

bitmap = [i]*64
koordinater = []
trekk = []

skjermHøyde = 800
skjermBredde = 800
skjerm = pg.display.set_mode([skjermBredde, skjermHøyde])

def tegnRuter(skjerm, bredde, høyde, liste):
    pixelhøyde = høyde//8
    pixelbredde = bredde//8
    for y in range(8):
        for x in range(8):
            rect = pg.Rect(x*pixelbredde, y*pixelhøyde, pixelbredde, pixelhøyde)
            pg.draw.rect(skjerm, (36, 135, 89) if (x+y)%2 == 0 else (36, 158, 89), rect)
            liste.append(rect.center)

class Spiller():
    def __init__(self, score, farge, symbol):
        self.farge = farge
        self.score = score
        self.symbol = symbol

    def plasserBrikke(self, skjerm, liste, bitmap, trekk):
        mus = pg.mouse.get_pos()
        mus_trykket = pg.mouse.get_pressed()
        rutenummer = -1

        for i in range(len(liste)):
            if abs(mus[0] - liste[i][0]) < 50 and abs(mus[1] - liste[i][1]) < 50:
                rutenummer = i
                break

        if rutenummer != -1 and mus_trykket[0] == True and bitmap[rutenummer] == "ingenting":
            if self.symbol == x:
                trekk.append((self.farge, liste[rutenummer], "x"))
            else:
                trekk.append((self.farge, liste[rutenummer], "o"))
            bitmap[rutenummer] = self.symbol

def tegnTrekk(skjerm, trekk):
    for farge, pos, symbol in trekk:
        if symbol == "x":
            pg.draw.line(skjerm, farge, (pos[0]-40, pos[1]-40), (pos[0]+40, pos[1]+40), 5)
            pg.draw.line(skjerm, farge, (pos[0]+40, pos[1]-40), (pos[0]-40, pos[1]+40), 5)
        else:
            pg.draw.circle(skjerm, farge, pos, 40, 5)

spiller = Spiller(2, (255,255,255), o)
spiller2 = Spiller(2,(0,0,0), x)

spillere = [spiller, spiller2]
spiller_index = 0

kjør = True

while kjør:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            kjør = False

    skjerm.fill((0, 0, 0))
    koordinater = []
    tegnRuter(skjerm, skjermBredde, skjermHøyde, koordinater)
    spillere[spiller_index].plasserBrikke(skjerm, koordinater, bitmap, trekk)
    tegnTrekk(skjerm, trekk)
    pg.display.flip()

    if pg.mouse.get_pressed()[0]:
        spiller_index = (spiller_index + 1) % 2

pg.quit()