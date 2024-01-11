import pygame
from fenetre import Fenetre
import sys
pygame.init()
# Définition de la classe Personnage
class Personnage:
    def __init__(self, type, image):
        self.fenetre = Fenetre()
        self.type = type
        self.image = pygame.image.load(image)
# Définition de la classe PokemonChoix
class PokemonChoix:
    def __init__(self):
        pass
# Définir la taille de la fenêtre
taille_fenetre = (800, 600)
fenetre = pygame.display.set_mode(taille_fenetre)
# Charger l'image de fond
fond = pygame.image.load('images/img10.png')

# Obtenir les dimensions de l'image
largeur_image, hauteur_image = fond.get_size()

# Calculer le nouveau rapport largeur/hauteur pour l'image
nouvelle_hauteur = int(taille_fenetre[0] * hauteur_image / largeur_image)

# Redimensionner l'image en conservant ses proportions
fond = pygame.transform.scale(fond, (taille_fenetre[0], nouvelle_hauteur))

# Charger la musique
pygame.mixer.music.load('musique/musique1.mp3')
pygame.mixer.music.play(-1)  # Jouer la musique en boucle

# Charger l'image du titre, la réduire de moitié et la centrer
titre = pygame.image.load('images/titre1.png')
titre = pygame.transform.scale(titre, (titre.get_width() // 2, titre.get_height() // 2))
titre_rect = titre.get_rect(center=(taille_fenetre[0] // 2, taille_fenetre[1] // 2 - 210))

# Ajouter une case rectangulaire pour le texte de l'utilisateur
input_box = pygame.Rect(taille_fenetre[0] // 2 - 130, taille_fenetre[1] // 2 + 80, 260, 30)

# Charger la police personnalisée
police = pygame.font.Font('font/PokemonClassic.ttf', 13)  # Taille du texte modifiée à 20pt

# Créer le texte
texte = police.render("Rentre le nom de ton personnage et clique sur son avatar", True, (255, 255, 255))

# Obtenir un rectangle qui encadre le texte
texte_rect = texte.get_rect()

# Centrer le rectangle horizontalement et le positionner à 10px au-dessus de la case noire
texte_rect.centerx = taille_fenetre[0] // 2
texte_rect.bottom = input_box.top - 10

# Créer les personnages et centrer leurs images en hauteur
fille = Personnage('fille', 'images/perso1.png')
fille.image = pygame.transform.scale(fille.image, (int(fille.image.get_width() * 0.45), int(fille.image.get_height() * 0.45)))
garcon = Personnage('garcon', 'images/perso2.png')
garcon.image = pygame.transform.scale(garcon.image, (int(garcon.image.get_width() * 0.45), int(garcon.image.get_height() * 0.45)))

# Calculer l'espace entre les images et les côtés de la fenêtre
largeur_fenetre = taille_fenetre[0]
largeur_image_fille = fille.image.get_width()
largeur_image_garcon = garcon.image.get_width()
espace = (largeur_fenetre - largeur_image_fille - largeur_image_garcon) / 3

# Positionner les images
fille_rect = fille.image.get_rect(center=(espace + largeur_image_fille / 2, taille_fenetre[1] // 2 - 65))
garcon_rect = garcon.image.get_rect(center=(2 * espace + largeur_image_fille + largeur_image_garcon / 2, taille_fenetre[1] // 2 - 65))

color_inactive = pygame.Color('black')
color_active = pygame.Color('lightgreen')
color = color_inactive
active = False
text = ''
font = pygame.font.Font('font/PokemonClassic.ttf', 13)

# Boucle principale
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

    fenetre.fill((255, 255, 255))
    fenetre.blit(fond, (0, 0))
    fenetre.blit(titre, titre_rect)
    fenetre.blit(texte, texte_rect)
    fenetre.blit(fille.image, fille_rect)
    fenetre.blit(garcon.image, garcon_rect)
    pygame.draw.rect(fenetre, color, input_box, 2)

    # Utiliser la variable 'font' pour la police de l'utilisateur
    txt_surface = font.render(text, True, color_active)
    txt_rect = txt_surface.get_rect()
    txt_rect.center = input_box.center
    fenetre.blit(txt_surface, txt_rect.topleft)

    pygame.display.flip()
    pygame.time.Clock().tick(30)