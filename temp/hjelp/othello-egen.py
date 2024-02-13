import pygame
import pygame.freetype

# Initialiser pygame
pygame.init()

# Sett skjermstørrelsen
skjerm_bredde = 600
skjerm_høyde = 400
skjerm = pygame.display.set_mode((skjerm_bredde, skjerm_høyde))

# Sett størrelsen på hver rute i rutenettet
rute_bredde = skjerm_bredde // 8
rute_høyde = skjerm_høyde // 8

# Definer fargene
mørkegrønn = (0, 100, 0)
lysegrønn = (0, 255, 0)

# Definer Spiller klassen
class Spiller:
    def __init__(self, symbol):
        self.symbol = symbol

# Opprett spillere
spillere = [Spiller('X'), Spiller('O')]
spiller_tur = 0

# Initialiser font
font = pygame.freetype.SysFont(None, 24)

# Opprett brettet
brett = [['' for _ in range(8)] for _ in range(8)]

# Sjekk om det er fire på rad
def sjekk_fire_på_rad(brett, symbol):
    # Sjekk horisontale linjer
    for rad in brett:
        for i in range(len(rad) - 3):
            if rad[i] == rad[i + 1] == rad[i + 2] == rad[i + 3] == symbol:
                return True

    # Sjekk vertikale linjer
    for kolonne in range(len(brett[0])):
        for i in range(len(brett) - 3):
            if brett[i][kolonne] == brett[i + 1][kolonne] == brett[i + 2][kolonne] == brett[i + 3][kolonne] == symbol:
                return True

    return False

# Hovedløkken
kjør = True
while kjør:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            kjør = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            rute_x = x // rute_bredde
            rute_y = y // rute_høyde
            brett[rute_y][rute_x] = spillere[spiller_tur].symbol
            font.render_to(skjerm, (rute_x * rute_bredde + rute_bredde // 2.5, rute_y * rute_høyde + rute_høyde // 2.5), spillere[spiller_tur].symbol, (255, 255, 255))
            if sjekk_fire_på_rad(brett, spillere[spiller_tur].symbol):
                print(f"Spiller {spillere[spiller_tur].symbol} har fire på rad!")
            spiller_tur = (spiller_tur + 1) % 2

    # Tegn rutenettet
    for i in range(8):
        for j in range(8):
            farge = mørkegrønn if (i + j) % 2 == 0 else lysegrønn
            pygame.draw.rect(skjerm, farge, pygame.Rect(i * rute_bredde, j * rute_høyde, rute_bredde, rute_høyde))

    # Oppdater skjermen
    pygame.display.flip()

# Avslutt pygame
pygame.quit()