import pygame
import math

class Menu:
    def __init__(self, ecran):
        self.ecran = ecran
        self.background = pygame.image.load("imagesM/fond-menu2.jpg").convert()
        self.background = pygame.transform.scale(self.background, (800, 600))
        self.bgX = 0
        self.font = pygame.font.Font("fontM/PokemonClassic.ttf", 11)

    def draw_background(self):
        self.ecran.blit(self.background, (self.bgX, 0))
        self.ecran.blit(self.background, (self.bgX + self.background.get_width(), 0))
        if self.bgX <= -self.background.get_width():
            self.bgX = 0

    def Musique(self):
        pygame.mixer.music.load('musiqueM/musique2.mp3')
        pygame.mixer.music.play(-1)

    def titre(self):
        image = pygame.image.load("imagesM/txt1.png").convert_alpha()
        largeur_originale, hauteur_originale = image.get_size()
        rapport = 500 / largeur_originale
        nouvelle_hauteur = int(hauteur_originale * rapport)
        image = pygame.transform.scale(image, (500, nouvelle_hauteur))
        return image

    def rounded_rect(self, surface, rect, color, radius=20):
        x, y, w, h = rect
        border_radius = radius
        pygame.draw.rect(surface, color, rect, border_radius=border_radius)
        # Pour plus de détails sur pygame.draw.rect et ses options, veuillez consulter la documentation officielle de Pygame.

    def cases(self, longueur, largeur, couleur, texte):
        text = self.font.render(texte, True, (255, 255, 255))
        text_rect = text.get_rect(center=(longueur + 100, largeur + 25))
        self.rounded_rect(self.ecran, (longueur, largeur, 200, 50), couleur, 20)
        self.ecran.blit(text, text_rect)

    def run(self):
        running = True
        self.Musique()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quitter"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 300 <= x <= 500 and 200 <= y <= 250:
                        return "personnage"
                    elif 300 <= x <= 500 and 300 <= y <= 350:
                        return "ajouterpokemon"
                    elif 300 <= x <= 500 and 400 <= y <= 450:
                        return "pokedex"
            self.bgX -= 0.2
            self.draw_background()
            titre = self.titre()
            largeur_titre, _ = titre.get_size()
            position_x = (800 - largeur_titre) // 2
            position_y = 100
            self.ecran.blit(titre, (position_x, position_y))
            self.cases(300, 200, (0, 0, 0), "Lancer la partie")
            self.cases(300, 300, (0, 0, 0), "Ajouter un Pokémon")
            self.cases(300, 400, (0, 0, 0), "Ouvrir le Pokédex")
            pygame.display.flip()

        return "quitter"
