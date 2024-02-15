# Importation des bibliothèques nécessaires
import pygame
import math

# Définition de la classe Menu
class Menu:
    # Initialisation de la classe
    def __init__(self, ecran):
        self.ecran = ecran  # L'écran sur lequel le menu sera affiché
        # Chargement et redimensionnement de l'image de fond
        self.background = pygame.image.load("imagesM/fond-menu2.jpg").convert()
        self.background = pygame.transform.scale(self.background, (800, 600))
        self.bgX = 0  # Position initiale de l'image de fond
        # Définition de la police utilisée pour le texte
        self.font = pygame.font.Font("fontM/PokemonClassic.ttf", 11)

    # Méthode pour dessiner l'image de fond
    def draw_background(self):
        # Affichage de l'image de fond à la position actuelle
        self.ecran.blit(self.background, (self.bgX, 0))
        # Affichage d'une deuxième image de fond à la suite de la première pour créer un effet de défilement
        self.ecran.blit(self.background, (self.bgX + self.background.get_width(), 0))
        # Réinitialisation de la position de l'image de fond si elle a entièrement défilé
        if self.bgX <= -self.background.get_width():
            self.bgX = 0

    # Méthode pour jouer la musique
    def Musique(self):
        pygame.mixer.music.load('musiqueM/musique2.mp3')  # Chargement de la musique
        pygame.mixer.music.play(-1)  # Lecture de la musique en boucle

    # Méthode pour créer le titre du menu
    def titre(self):
        # Chargement de l'image du titre
        image = pygame.image.load("imagesM/txt1.png").convert_alpha()
        # Redimensionnement de l'image du titre pour qu'elle ait une largeur de 500 pixels tout en conservant les proportions
        largeur_originale, hauteur_originale = image.get_size()
        rapport = 500 / largeur_originale
        nouvelle_hauteur = int(hauteur_originale * rapport)
        image = pygame.transform.scale(image, (500, nouvelle_hauteur))
        return image

    # Méthode pour dessiner un rectangle arrondi
    def rounded_rect(self, surface, rect, color, radius=20):
        x, y, w, h = rect
        border_radius = radius
        pygame.draw.rect(surface, color, rect, border_radius=border_radius)
        # Pour plus de détails sur pygame.draw.rect et ses options, veuillez consulter la documentation officielle de Pygame.

    # Méthode pour créer les cases du menu
    def cases(self, longueur, largeur, couleur, texte):
        # Création du texte à afficher dans la case
        text = self.font.render(texte, True, (255, 255, 255))
        # Positionnement du texte au centre de la case
        text_rect = text.get_rect(center=(longueur + 100, largeur + 25))
        # Dessin de la case
        self.rounded_rect(self.ecran, (longueur, largeur, 200, 50), couleur, 20)
        # Affichage du texte dans la case
        self.ecran.blit(text, text_rect)

    # Méthode pour exécuter le menu
    def run(self):
        running = True
        self.Musique()  # Lancement de la musique
        while running:
            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quitter"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    # Si l'utilisateur clique sur la première case, on lance la partie
                    if 300 <= x <= 500 and 200 <= y <= 250:
                        return "personnage"
                    # Si l'utilisateur clique sur la deuxième case, on ajoute un Pokémon
                    elif 300 <= x <= 500 and 300 <= y <= 350:
                        return "ajouterpokemon"
                    # Si l'utilisateur clique sur la troisième case, on ouvre le Pokédex
                    elif 300 <= x <= 500 and 400 <= y <= 450:
                        return "pokedex"
            # Mise à jour de la position de l'image de fond pour créer l'effet de défilement
            self.bgX -= 0.2
            # Dessin de l'image de fond
            self.draw_background()
            # Création et affichage du titre
            titre = self.titre()
            largeur_titre, _ = titre.get_size()
            position_x = (800 - largeur_titre) // 2
            position_y = 100
            self.ecran.blit(titre, (position_x, position_y))
            # Création et affichage des cases du menu
            self.cases(300, 200, (0, 0, 0), "Lancer la partie")
            self.cases(300, 300, (0, 0, 0), "Ajouter un Pokémon")
            self.cases(300, 400, (0, 0, 0), "Ouvrir le Pokédex")
            # Mise à jour de l'affichage
            pygame.display.flip()

        return "quitter"
