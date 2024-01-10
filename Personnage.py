import pygame
from fenetre import Fenetre
import sys

pygame.init()

class Personnage:
    def __init__(self, type, image):
        self.fenetre = Fenetre()
        self.type = type
        self.image = pygame.image.load(image)

class PokemonChoix:
    def __init__(self):
        pass
        # Ajoutez ici le code pour la nouvelle page

# Définir la taille de la fenêtre
taille_fenetre = (800, 600)
fenetre = pygame.display.set_mode(taille_fenetre)

# Charger l'image de fond et l'adapter à la taille de la fenêtre
fond = pygame.image.load('images/img1.jpg')
fond = pygame.transform.scale(fond, taille_fenetre)

# Charger la musique
pygame.mixer.music.load('musique/musique1.mp3')
pygame.mixer.music.play(-1)  # Jouer la musique en boucle

# Charger l'image du titre, la réduire de moitié et la centrer
titre = pygame.image.load('images/titre1.png')
titre = pygame.transform.scale(titre, (titre.get_width() // 2, titre.get_height() // 2))
titre_rect = titre.get_rect(center=(taille_fenetre[0] // 2, taille_fenetre[1] // 2))

# Définir la police pour le texte
police = pygame.font.Font(None, 36)

# Créer le texte
texte = police.render("Rentre le nom de ton personnage et clique sur son avatar", True, (255, 255, 255))

# Créer les personnages et centrer leurs images en hauteur
fille = Personnage('fille', 'images/perso1.png')
fille.image = pygame.transform.scale(fille.image, (fille.image.get_width() // 3, fille.image.get_height() // 3))
fille_rect = fille.image.get_rect(center=(200, taille_fenetre[1] // 2))

garcon = Personnage('garcon', 'images/perso2.png')
garcon.image = pygame.transform.scale(garcon.image, (garcon.image.get_width() // 3, garcon.image.get_height() // 3))
garcon_rect = garcon.image.get_rect(center=(500, taille_fenetre[1] // 2))

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            # Ajoutez ici le code pour vérifier si l'utilisateur a cliqué sur une image de personnage

    # Dessiner l'image de fond
    fenetre.blit(fond, (0, 0))

    # Dessiner l'image du titre centrée
    fenetre.blit(titre, titre_rect)

    # Dessiner le texte
    fenetre.blit(texte, (300, 100))

    # Dessiner les images des personnages centrées en hauteur
    fenetre.blit(fille.image, fille_rect)
    fenetre.blit(garcon.image, garcon_rect)

    # Mettre à jour l'affichage
    pygame.display.flip()

