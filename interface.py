import pygame
from pygame import Rect
from fenetre import Fenetre
from sprites import Sprites
import json

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 200, 0)
red = (200, 0, 0)
dark_grey = (50, 50, 50)
light_grey = (150, 150, 150)
yellow = (222, 193, 96)

# Charger le fichier JSON
with open('pokedex.json', encoding='utf-8') as f:
        data = json.load(f)

# Récupérer les attaques du Pokémon
pokemon = data["Pikachu"]
attacks = pokemon["attacks"]

class Interface:
    # Initialise l'interface avec une fenêtre, des coordonnées, un fichier json et des états
    def __init__(self, fenetre, x, y, x2, y2, json_file):
        self.fenetre = fenetre
        self.sprites = Sprites(x, y, x2, y2, json_file)
        self.nb_potions = 3
        self.attaquer = True
        self.sac = True
        self.utiliser_potion = False
        self.utiliser_attaques = False
        
    def run(self):
        # Créé les boutons et gestion de la boucle principale du jeu
        bouton_attaquer = self.create_bouton(180, 90, 410, 390, 410 + 180/2, 390 + 90/2, "Attaquer")
        bouton_sac = self.create_bouton(180, 90, 600, 390, 600 + 180/2, 390 + 90/2, "Sac")
        bouton_utiliser_potion = self.create_bouton(180, 90, 410, 390, 410 + 180/2, 390 + 90/2, f"Potions ({self.nb_potions})")
        bouton_retour = self.create_bouton(180, 90, 600, 390, 600 + 180/2, 390 + 90/2, "Retour")
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return "quitter"

                # Gestion des événements pour le sac et les attaques
                if self.utiliser_potion or self.utiliser_attaques:
                    self.retour(event, bouton_retour, bouton_utiliser_potion)
                else:
                    self.use_sac(event, bouton_sac)
                    self.use_attaques(event, bouton_attaquer)

            # Mettre à jour l'affichage ici
            self.interface()

        # Autres opérations de nettoyage si nécessaire
        return "menu"
    
    def retour(self, event, bouton_retour, bouton_utiliser_potion):
        # Gère les événements de retour et d'utilisation de potion
        if event.type == pygame.MOUSEBUTTONDOWN:
            if bouton_retour.collidepoint(event.pos):
                # Si l'utilisateur clique sur "Retour", revenir à précédent
                self.attaquer = True
                self.sac = True
                self.utiliser_potion = False
                self.utiliser_attaques = False
            elif bouton_utiliser_potion and bouton_utiliser_potion.collidepoint(event.pos):
                # Si l'utilisateur clique sur "Utiliser Potion"
                if self.nb_potions > 0:
                    # Logique pour utiliser une potion
                    self.nb_potions -= 1
                    # Vous pouvez ajouter ici une logique pour l'effet de la potion

            pygame.display.flip()

    def draw_pv(self):
        # Dessiner la barre de vie du premier Pokémon
        health_bar = pygame.image.load("images-i/Health-bar.png").convert_alpha()
        new_height = int(220 * health_bar.get_height() / health_bar.get_width())
        health_bar = pygame.transform.scale(health_bar, (220, new_height))
        position_health_bar = (0, 130)

        if self.sprites.current_pokemon == "Dracaufeu":  # Utilisation de l'attribut current_pokemon
            position_health_bar = (0, 160)

        self.fenetre.ecran.blit(health_bar, position_health_bar)

        pygame.draw.rect(self.fenetre.ecran, red, (91, 174, 86, 5), 0)
        pygame.draw.rect(self.fenetre.ecran, green, (91, 174, 86, 5), 0)

        # Dessiner la barre de vie du deuxième Pokémon
        health_bar_adverse = pygame.image.load("images-i/Health-bar-adverse.png").convert_alpha()
        new_height_adverse = int(220 * health_bar_adverse.get_height() / health_bar_adverse.get_width())
        health_bar_adverse = pygame.transform.scale(health_bar_adverse, (220, new_height_adverse))
        position_health_bar_adverse = (580, 35)

        if self.sprites.random_pokemon == "Dracaufeu":
            position_health_bar_adverse = (580, 15) 

        self.fenetre.ecran.blit(health_bar_adverse, position_health_bar_adverse)

        pygame.draw.rect(self.fenetre.ecran, red, (703, 78, 22, 5), 0)
        pygame.draw.rect(self.fenetre.ecran, green, (703, 78, 82, 5), 0)

    def interface(self):
        # gère l'interface graphique
        background = pygame.image.load("images-i/Battle-Background.png").convert_alpha()

        # Redimensionne l'image d'arrière-plan pour qu'elle ait la même largeur que le rectangle
        background = pygame.transform.scale(background, (800, int(660 * background.get_height() / background.get_width())))

        # Dessiner l'image d'arrière-plan par-dessus le rectangle
        self.fenetre.ecran.blit(background, (0, 0))

        self.sprites.draw()
        self.sprites.draw2()
        self.draw_pv()

        # Dessine le rectangle gris en fond
        pygame.draw.rect(self.fenetre.ecran, dark_grey, (0, 370, 800, 130))
        # Dessine à droite le rectangle jaune en premier
        pygame.draw.rect(self.fenetre.ecran, yellow, (10, 380, 380, 110), 0, 4)
        # Dessine à droite le rectangle blanc par-dessus
        pygame.draw.rect(self.fenetre.ecran, white, (15, 385, 370, 100), 0, 4)
        # Dessine à gauche le rectangle gris clair par-dessus
        pygame.draw.rect(self.fenetre.ecran, light_grey, (400, 380, 390, 110), 0, 4)

        if self.attaquer == True:
            # Si 'attaquer' est actif, un bouton "Attaquer" est créé avec les dimensions et la position spécifiées.
            self.create_bouton(180, 90, 410, 390, 410 + 180/2, 390 + 90/2, "Attaquer")

        if self.sac == True:
            # Si 'sac' est actif, un bouton "Sac" est créé avec les dimensions et la position spécifiées.
            self.create_bouton(180, 90, 600, 390, 600 + 180/2, 390 + 90/2, "Sac")

        if self.utiliser_potion == True:
            # Si 'utiliser_potion' est actif, deux boutons sont créés : "Potions" et "Retour", avec les dimensions et la position spécifiées.
            self.create_bouton(180, 90, 410, 390, 410 + 180/2, 390 + 90/2, f"Potions ({self.nb_potions})")
            self.create_bouton(180, 90, 600, 390, 600 + 180/2, 390 + 90/2, "Retour")

        if self.utiliser_attaques == True:
            # Si 'utiliser_attaques' est actif, un bouton est créé pour chaque attaque dans la liste des attaques du pokemon dans le fichier json
            for i in range(len(attacks)):
                self.create_bouton(180, 45, 410 + (i % 2) * 190, 390 + (i // 2) * 50, 410 + (i % 2) * 190 + 180/2, 415 + (i // 2) * 50, attacks[i]["name"])

        pygame.display.flip()

    def create_bouton(self, width, height, left, top, text_cx, text_cy, label):
        # Création des boutons avec une taille, une position et un label
        pos_souris = pygame.mouse.get_pos()
        
        bouton = Rect(left, top, width, height)
        
        # surbrillance du bouton si la souris est dessus
        if bouton.collidepoint(pos_souris):
            pygame.draw.rect(self.fenetre.ecran, yellow, bouton)
        else:
            pygame.draw.rect(self.fenetre.ecran, white, bouton)
            
        # ajouter le texte du bouton
        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text = font.render(f'{label}', True, black)
        text_rect = text.get_rect(center=(text_cx, text_cy))
        self.fenetre.ecran.blit(text, text_rect)
        
        return bouton
    
    def use_sac(self, event, bouton_sac):
        # Gère l'utilisation du sac
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Si l'utilisateur clique sur le bouton "Sac"...
            if bouton_sac.collidepoint(event.pos):
                # ... alors on désactive les états "attaquer" et "sac" et on active l'état "utiliser_potion".
                self.attaquer = False
                self.sac = False
                self.utiliser_potion = True

        pygame.display.flip()

    def use_attaques(self, event, bouton_attaquer):
        # Gere l'utilisation des attaques
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Si l'utilisateur clique sur le bouton "Attaquer"...
            if bouton_attaquer.collidepoint(event.pos):
                # on désactive les états "attaquer", "sac" et "utiliser_potion" et on active l'état "utiliser_attaques".
                self.attaquer = False
                self.sac = False
                self.utiliser_potion = False
                self.utiliser_attaques = True
                print("attaquer")

        pygame.display.flip()
