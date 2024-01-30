import pygame

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
            print(f"Spilleren trykket på rute ({rute_x}, {rute_y})")

    # Tegn rutenettet
    for i in range(8):
        for j in range(8):
            farge = mørkegrønn if (i + j) % 2 == 0 else lysegrønn
            pygame.draw.rect(skjerm, farge, pygame.Rect(i * rute_bredde, j * rute_høyde, rute_bredde, rute_høyde))

    # Oppdater skjermen
    pygame.display.flip()

# Avslutt pygame
pygame.quit()