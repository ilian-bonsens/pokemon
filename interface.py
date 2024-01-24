import pygame
from pygame import Rect
from fenetre import Fenetre
from sprites import Sprites

pygame.init()

fenetre = Fenetre()

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 200, 0)
red = (200, 0, 0)
dark_grey = (50, 50, 50)
light_grey = (150, 150, 150)
yellow = (222, 193, 96)

class Interface:
    def __init__(self, x, y, x2, y2, json_file):
        self.sprites = Sprites(x, y, x2, y2, json_file)
        self.nb_potions = 4
        self.attaquer = True
        self.potions = True
        self.utiliser_potion = False

    def draw_pv(self):
        # Dessiner la barre de vie du premier Pokémon
        health_bar = pygame.image.load("images-i/Health-bar.png").convert_alpha()
        new_height = int(220 * health_bar.get_height() / health_bar.get_width())
        health_bar = pygame.transform.scale(health_bar, (220, new_height))
        position_health_bar = (0, 130)
        if self.sprites.current_pokemon == "Dracaufeu":  # Utilisation de l'attribut current_pokemon
            position_health_bar = (0, 160)
        fenetre.ecran.blit(health_bar, position_health_bar)
        pygame.draw.rect(fenetre.ecran, red, (91, 174, 86, 5), 0)
        pygame.draw.rect(fenetre.ecran, green, (91, 174, 86, 5), 0)

        # Dessiner la barre de vie du deuxième Pokémon
        health_bar_adverse = pygame.image.load("images-i/Health-bar-adverse.png").convert_alpha()
        new_height_adverse = int(220 * health_bar_adverse.get_height() / health_bar_adverse.get_width())
        health_bar_adverse = pygame.transform.scale(health_bar_adverse, (220, new_height_adverse))
        position_health_bar_adverse = (580, 35)
        if self.sprites.random_pokemon == "Dracaufeu":
            position_health_bar_adverse = (580, 15) 
        fenetre.ecran.blit(health_bar_adverse, position_health_bar_adverse)
        pygame.draw.rect(fenetre.ecran, red, (703, 78, 22, 5), 0)
        pygame.draw.rect(fenetre.ecran, green, (703, 78, 82, 5), 0)

    def interface(self):
        # Charger l'image d'arrière-plan
        background = pygame.image.load("images-i/Battle-Background.png").convert_alpha()

        # Redimensionner l'image d'arrière-plan pour qu'elle ait la même largeur que le rectangle
        background = pygame.transform.scale(background, (800, int(660 * background.get_height() / background.get_width())))

        # Dessiner l'image d'arrière-plan par-dessus le rectangle
        fenetre.ecran.blit(background, (0, 0))

        self.sprites.draw()
        self.sprites.draw2()
        self.draw_pv()

        # Dessine le rectangle gris en fond
        pygame.draw.rect(fenetre.ecran, dark_grey, (0, 370, 800, 130))
        # Dessine à droite le rectangle jaune en premier
        pygame.draw.rect(fenetre.ecran, yellow, (10, 380, 380, 110), 0, 4)
        # Dessine à droite le rectangle blanc par-dessus
        pygame.draw.rect(fenetre.ecran, white, (15, 385, 370, 100), 0, 4)
        # Dessine à gauche le rectangle gris clair par-dessus
        pygame.draw.rect(fenetre.ecran, light_grey, (400, 380, 390, 110), 0, 4)

        if self.attaquer == True:
            self.create_bouton(180, 90, 410, 390, 410 + 180/2, 390 + 90/2, "Attaquer")
        if self.potions == True:
            self.create_bouton(180, 90, 600, 390, 600 + 180/2, 390 + 90/2, "Potions")
        if self.utiliser_potion == True:  # Vérifiez l'état du bouton "Utiliser une potion"
            self.create_bouton(360, 90, 410, 390, 410 + 360/2, 390 + 90/2, f"Utiliser une potion ({self.nb_potions})")

        pygame.display.flip()

    def create_bouton(self, width, height, left, top, text_cx, text_cy, label):  # Ajout de 'self'
        # position de la souris
        pos_souris = pygame.mouse.get_pos()
        
        bouton = Rect(left, top, width, height)
        
        # surbrillance du bouton si la souris est dessus
        if bouton.collidepoint(pos_souris):
            pygame.draw.rect(fenetre.ecran, yellow, bouton)
        else:
            pygame.draw.rect(fenetre.ecran, white, bouton)
            
        # ajouter le texte du bouton
        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text = font.render(f'{label}', True, black)
        text_rect = text.get_rect(center=(text_cx, text_cy))
        fenetre.ecran.blit(text, text_rect)
        
        return bouton
    
    def use_potions(self, event, bouton_attaquer, bouton_potions):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if bouton_potions.collidepoint(event.pos):
                if self.nb_potions > 0 :
                    self.nb_potions -= 1
                self.attaquer = False
                self.potions = False
                if self.potions == False:
                    self.utiliser_potion = True  # Mettez à jour l'état du bouton "Utiliser une potion"
                pygame.display.flip()


combat = Interface(300, 300, 400, 400, 'pokedex.json')

bouton_attaquer = combat.create_bouton(180, 90, 410, 390, 410 + 180/2, 390 + 90/2, "Attaquer")
bouton_potions = combat.create_bouton(180, 90, 600, 390, 600 + 180/2, 390 + 90/2, "Potions")
bouton_utiliser_potion = combat.create_bouton(360, 90, 410, 390, 410 + 360/2, 390 + 90/2, f"Utiliser une potion ({combat.nb_potions})")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            combat.use_potions(event, bouton_attaquer, bouton_potions)
    combat.interface()

pygame.quit()
