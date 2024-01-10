import pygame

class Fenetre:
    def __init__(self):
        self.largeur = 800
        self.hauteur = 500
        self.ecran = pygame.display.set_mode((self.largeur, self.hauteur))
        self.framerate = 60
        pygame.display.set_caption("Pokémon IML V1")
        pygame.display.set_icon(pygame.image.load("images-menu/icone.png"))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.flip()
        pygame.quit()

