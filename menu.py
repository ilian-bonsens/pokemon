import pygame
from fenetre import Fenetre
import math

pygame.init()
pygame.mixer.init()  # Ajoutez cette ligne pour initialiser le mixer de pygame

class Menu:
    def __init__(self):
        self.fenetre = Fenetre()
        self.background = pygame.image.load("images-menu/fond-menu2.jpg")
        self.background = pygame.transform.scale(self.background,(self.fenetre.largeur, self.fenetre.hauteur))
        self.bgX = 0
        self.time = 0 #ajout de l'animation de l'image
        self.font = pygame.font.Font("fonts/PokemonClassic.ttf", 11) #ajout pour le texte
        
    def draw_background(self):
        self.fenetre.ecran.blit(self.background, (self.bgX, 0))
        self.fenetre.ecran.blit(self.background, (self.bgX + self.background.get_width(), 0))
        if self.bgX <= -self.background.get_width():
            self.fenetre.ecran.blit(self.background, (self.bgX + 2*self.background.get_width(), 0))

    def Musique(self):
        pygame.mixer.music.load('music/Pokemonmusic1.mp3')  
        pygame.mixer.music.play(-1)  # Joue la musique en boucle   

    def titre(self):
        image = pygame.image.load("images-menu/titre2.png")
        largeur_image, hauteur_image = image.get_size()
        largeur_image //= 1.5
        hauteur_image //= 1.5
        image = pygame.transform.scale(image, (largeur_image, hauteur_image)) 
        return image
    
    def rounded_rect(self, surface, rect, color, radius=10):
        """ Draw a rectangle with rounded corners """
        rect = pygame.Rect(rect)
        circle = pygame.Surface([radius * 2, radius * 2])
        pygame.draw.ellipse(circle, (0, 0, 0, 0), circle.get_rect(), 0)
        pygame.draw.ellipse(circle, color, circle.get_rect(), 0)
        circle.set_colorkey((0, 0, 0, 0))

        surface.blit(pygame.transform.scale(circle, (radius, radius)), (rect.left, rect.top))
        surface.blit(pygame.transform.scale(circle, (radius, radius)), (rect.right - radius - 1, rect.top))
        surface.blit(pygame.transform.scale(circle, (radius, radius)), (rect.left, rect.bottom - radius - 1))
        surface.blit(pygame.transform.scale(circle, (radius, radius)), (rect.right - radius - 1, rect.bottom - radius - 1))

        surface.fill(color, rect.inflate(-radius * 2, 0))
        surface.fill(color, rect.inflate(0, -radius * 2))

    def cases(self, longueur, largeur, couleur, texte):
        surface = pygame.Surface((200, 50), pygame.SRCALPHA)  # Crée une surface transparente
        self.rounded_rect(surface, surface.get_rect(), couleur, 10)
        self.fenetre.ecran.blit(surface, (longueur, largeur))  # Affiche la surface sur l'écran
        text = self.font.render(texte, True, (255, 255, 255))  # Crée le texte
        text_rect = text.get_rect(center=(longueur + 100, largeur + 25))  # Centre le texte dans la case
        self.fenetre.ecran.blit(text, text_rect)  # Affiche le texte

    def run(self):
        running = True
        self.Musique()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

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

