import pygame

class Fenetre:
    def __init__(self):
        self.largeur = 800
        self.hauteur = 500
        self.ecran = pygame.display.set_mode((self.largeur, self.hauteur))
        self.framerate = 60
        pygame.display.set_caption("Pokémon IML V1")
        pygame.display.set_icon(pygame.image.load("icone/icone.png"))
