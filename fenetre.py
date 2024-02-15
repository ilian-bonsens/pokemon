# Importation du module pygame
import pygame

# Définition de la classe Fenetre
class Fenetre:
    def __init__(self):
        # Création d'une fenêtre de 800x500 pixels
        self.ecran = pygame.display.set_mode((800, 500))

        # Définition du taux de rafraîchissement à 60 images par seconde
        self.framerate = 60

        # Définition du titre de la fenêtre
        pygame.display.set_caption("Pokémon IML V1")

        # Définition de l'icône de la fenêtre
        pygame.display.set_icon(pygame.image.load("images-i/icone.png"))

    # Méthode pour exécuter la fenêtre
    def run(self):
        # Initialisation de la variable running à True pour démarrer la boucle principale
        running = True

        # Boucle principale de la fenêtre
        while running:
            # Parcours de tous les événements pygame
            for event in pygame.event.get():
                # Si l'événement est de type QUIT (fermeture de la fenêtre), on met running à False pour sortir de la boucle
                if event.type == pygame.QUIT:
                    running = False

            # Mise à jour de l'affichage
            pygame.display.flip()

        # Quitter pygame une fois que la boucle principale est terminée
        pygame.quit()