import pygame
from fenetre import Fenetre
import sys

# Initialisation du module pygame
pygame.init()

# Définition de la classe Personnage
class PokemonChoix:
    def __init__(self, type, image):
        self.fenetre = Fenetre()
        self.type = type
        self.image = pygame.image.load(image)


# Définition de la taille de la fenêtre
taille_fenetre = (800, 600)
fenetre = pygame.display.set_mode(taille_fenetre)

# Chargement de l'image de fond
fond = pygame.image.load('images/img10.png')

# Ajustement des dimensions de l'image de fond pour s'adapter à la fenêtre
largeur_image, hauteur_image = fond.get_size()
nouvelle_hauteur = int(taille_fenetre[0] * hauteur_image / largeur_image)
fond = pygame.transform.scale(fond, (taille_fenetre[0], nouvelle_hauteur))

# Chargement de la musique et lecture en boucle
pygame.mixer.music.load('musique/musique1.mp3')
pygame.mixer.music.play(-1)

# Chargement de l'image du titre, réduction de moitié et positionnement au centre
titre = pygame.image.load('images/titre1.png')
titre = pygame.transform.scale(titre, (titre.get_width() // 2, titre.get_height() // 2))
titre_rect = titre.get_rect(center=(taille_fenetre[0] // 2, taille_fenetre[1] // 2 - 210))

# Ajout d'une case rectangulaire pour le texte de l'utilisateur
input_box = pygame.Rect(taille_fenetre[0] // 2 - 130, taille_fenetre[1] // 2 + 80, 260, 30)

# Chargement de la police personnalisée
police = pygame.font.Font('font/PokemonClassic.ttf', 13)

# Création du texte informatif pour l'utilisateur
texte = police.render("Rentre le nom de ton personnage et clique sur son avatar", True, (255, 255, 255))
texte_rect = texte.get_rect()
texte_rect.centerx = taille_fenetre[0] // 2
texte_rect.bottom = input_box.top - 10

# Création des personnages (fille et garçon) et redimensionnement de leurs images
fille = Personnage('fille', 'images/perso1.png')
fille.image = pygame.transform.scale(fille.image, (int(fille.image.get_width() * 0.45), int(fille.image.get_height() * 0.45)))

garcon = Personnage('garcon', 'images/perso2.png')
garcon.image = pygame.transform.scale(garcon.image, (int(garcon.image.get_width() * 0.45), int(garcon.image.get_height() * 0.45)))

# Calcul de l'espace entre les images des personnages et les côtés de la fenêtre
largeur_fenetre = taille_fenetre[0]
largeur_image_fille = fille.image.get_width()
largeur_image_garcon = garcon.image.get_width()
espace = (largeur_fenetre - largeur_image_fille - largeur_image_garcon) / 3

# Positionnement des images des personnages
fille_rect = fille.image.get_rect(center=(espace + largeur_image_fille / 2, taille_fenetre[1] // 2 - 65))
garcon_rect = garcon.image.get_rect(center=(2 * espace + largeur_image_fille + largeur_image_garcon / 2, taille_fenetre[1] // 2 - 65))

# Définition des couleurs pour la case de texte
color_inactive = pygame.Color('black')
color_active = pygame.Color('lightgreen')
color_texte_utilisateur = pygame.Color('white')

# Boucle principale du jeu
active = False
text = ''
font = pygame.font.Font('font/PokemonClassic.ttf', 13)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if input_box.collidepoint(x, y):
                active = not active
            else:
                active = False
            color = color_active if active else color_inactive
        elif event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    print(text)
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    # Effacement de la fenêtre avec une couleur blanche
    fenetre.fill((255, 255, 255))

    # Dessin de l'image de fond
    fenetre.blit(fond, (0, 0))

    # Dessin du titre
    fenetre.blit(titre, titre_rect)

    # Dessin du texte informatif
    fenetre.blit(texte, texte_rect)

    # Dessin des images des personnages
    fenetre.blit(fille.image, fille_rect)
    fenetre.blit(garcon.image, garcon_rect)

    # Dessin de la case de texte
    pygame.draw.rect(fenetre, color_inactive, input_box)

    # Dessin du texte de l'utilisateur
    txt_surface = font.render(text, True, color_texte_utilisateur)
    txt_rect = txt_surface.get_rect()
    txt_rect.center = input_box.center
    fenetre.blit(txt_surface, txt_rect.topleft)

    # Mise à jour de l'affichage
    pygame.display.flip()

    # Limite de rafraîchissement à 30 images par seconde
    pygame.time.Clock().tick(30)