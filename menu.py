import pygame
from fenetre import Fenetre
import math
from personnage import Personnage

pygame.init()
pygame.mixer.init()

class Menu:
    def __init__(self):
        self.fenetre = Fenetre()
        self.background = pygame.image.load("images-menu/fond-menu2.jpg")
        self.background = pygame.transform.scale(self.background, (self.fenetre.largeur, self.fenetre.hauteur))
        self.bgX = 0
        self.time = 0
        self.font = pygame.font.Font("fonts/PokemonClassic.ttf", 11)

    def draw_background(self):
        self.fenetre.ecran.blit(self.background, (self.bgX, 0))
        self.fenetre.ecran.blit(self.background, (self.bgX + self.background.get_width(), 0))
        if self.bgX <= -self.background.get_width():
            self.fenetre.ecran.blit(self.background, (self.bgX + 2 * self.background.get_width(), 0))

    def Musique(self):
        pygame.mixer.music.load('music/Pokemonmusic1.mp3')
        pygame.mixer.music.play(-1)

    def titre(self):
        image = pygame.image.load("images-menu/titre2.png")
        largeur_image, hauteur_image = image.get_size()
        largeur_image //= 1.5
        hauteur_image //= 1.5
        image = pygame.transform.scale(image, (largeur_image, hauteur_image))
        return image

    def rounded_rect(self, surface, rect, color, radius=20):
        rect = pygame.Rect(rect)
        color_surface = pygame.Surface(rect.size, pygame.SRCALPHA)
        color_surface.fill(color)
        tmp_rect = pygame.Rect(0, 0, radius, radius)
        corner = pygame.Surface(tmp_rect.size, pygame.SRCALPHA)

        pygame.draw.ellipse(corner, (0, 0, 0), tmp_rect)
        corner = pygame.transform.scale(corner, (radius, radius))

        for pos in ((0, 0), (rect.width - radius - 1, 0), (0, rect.height - radius - 1),
                    (rect.width - radius - 1, rect.height - radius - 1)):
            color_surface.blit(corner, pos)

        color_surface.fill((0, 0, 0), (radius, 0, rect.width - radius * 2, rect.height))
        color_surface.fill((0, 0, 0), (0, radius, rect.width, rect.height - radius * 2))

        surface.blit(color_surface, rect.topleft)

    def cases(self, longueur, largeur, couleur, texte):
        surface = pygame.Surface((200, 50), pygame.SRCALPHA)
        self.rounded_rect(surface, surface.get_rect(), couleur, 10)
        self.fenetre.ecran.blit(surface, (longueur, largeur))
        text = self.font.render(texte, True, (255, 255, 255))
        text_rect = text.get_rect(center=(longueur + 100, largeur + 25))
        self.fenetre.ecran.blit(text, text_rect)

    def transition_personnage(self):
        pygame.quit()
        personnage = Personnage()
        personnage.run()

    def run(self):
        running = True
        self.Musique()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 300 <= x <= 500 and 200 <= y <= 250:
                        self.transition_personnage()

            self.draw_background()
            self.bgX -= 0.03
            if self.bgX <= -self.background.get_width():
                self.bgX += self.background.get_width()

            titre = self.titre()
            largeur_titre, _ = titre.get_size()
            position_x = (self.fenetre.largeur - largeur_titre) // 2
            position_y = 30 + math.sin(self.time) * 10
            self.fenetre.ecran.blit(titre, (position_x, position_y))
            self.cases(300, 200, (0, 0, 0), "Lancer la partie")
            self.cases(300, 300, (0, 0, 0), "Ajouter un Pokémon")
            self.cases(300, 400, (0, 0, 0), "Ouvrir la Pokédex")

            self.time += 0.01

            pygame.display.flip()
        pygame.quit()

menu = Menu()
menu.run()
