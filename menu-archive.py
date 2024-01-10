import pygame
from fenetre import Fenetre

pygame.init()

class Menu:
    def __init__(self):
        self.fenetre = Fenetre()
        self.background = pygame.image.load("images-menu/background-menu.jpg")
        self.bgX = 0

    def draw_background(self):
        self.fenetre.ecran.blit(self.background, (self.bgX, 0))
        self.fenetre.ecran.blit(self.background, (self.bgX + self.background.get_width(), 0))

    def titre(self):
        font = pygame.font.Font("fonts/Pokemon Solid.ttf", 63)
        titre = font.render("Pokémon IML", True, (199, 160, 8))
        return titre

    def cases(self, longueur, largeur, couleur):
        pygame.draw.rect(self.fenetre.ecran, couleur, (longueur, largeur, 200, 50))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.draw_background()
            self.bgX -= 0.1
            if self.bgX >= self.background.get_width():
                self.bgX = 0

            titre = self.titre()
            self.fenetre.ecran.blit(titre, (200, 30))
            self.cases(300, 200, (200, 200, 200))
            self.cases(300, 300, (200, 200, 200)) 
            self.cases(300, 400, (200, 200, 200)) 

            pygame.display.flip()
        pygame.quit()

menu = Menu()
menu.run()



