import pygame

class ChoixPokemon:
    def __init__(self, ecran):
        # Initialisation de l'écran sur lequel les éléments graphiques seront affichés
        self.ecran = ecran 
        # Initialisation de la variable qui gardera en mémoire le Pokémon sélectionné par l'utilisateur
        self.pokemon_selectionne = None

    def run(self): # Méthode principale qui lance l'interface de choix de Pokémon
        taille_fenetre = (800, 600)
        fond = pygame.image.load('imagesM/fond3.png')
        fond = pygame.transform.scale(fond, taille_fenetre)

        # Chargement et lecture en boucle de la musique de fond
        pygame.mixer.music.load('musiqueM/Pokemonmusic1.mp3')
        pygame.mixer.music.play(-1)

        # Chargement de l'image du titre, ajustement de sa taille et positionnement au centre en haut
        titre = pygame.image.load('imagesM/txt3.png')
        rapport = 550 / titre.get_width()
        nouvelle_hauteur = int(titre.get_height() * rapport)
        titre = pygame.transform.scale(titre, (550, nouvelle_hauteur))
        titre_rect = titre.get_rect(center=(taille_fenetre[0] // 2, 100))

        # Chargement et redimensionnement des images des Pokémon
        noms_pokemon = ['carapuce.png', 'pikachu.png', 'salameche.png', 'bulbizarre.png']
        images_pokemon = [pygame.image.load(f'imagesM/{nom}') for nom in noms_pokemon]
        rapports = [200 / img.get_height() for img in images_pokemon]
        nouvelles_largeurs = [int(img.get_width() * rapport) for img, rapport in zip(images_pokemon, rapports)]
        images_pokemon = [pygame.transform.scale(img, (largeur, 200)) for img, largeur in zip(images_pokemon, nouvelles_largeurs)]

        # Calcul des positions pour les images de Pokémon
        largeur_totale_images = sum(nouvelles_largeurs)
        espacement = (taille_fenetre[0] - largeur_totale_images) // (len(images_pokemon) + 1)
        pokemon_rects = []
        for i in range(4):
            x = espacement + i * (nouvelles_largeurs[0] + espacement)
            rect = images_pokemon[i].get_rect(topleft=(x, 150))
            pokemon_rects.append(rect)

        # Couleur utilisée pour indiquer le Pokémon sélectionné
        color_active = pygame.Color(255, 0, 0)

        # Boucle principale de l'interface
        running = True
        while running:
            # Gestion des événements (fermeture de la fenêtre, clics de souris)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quitter"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    for i, rect in enumerate(pokemon_rects):
                        if rect.collidepoint(x, y):
                            pokemon_nom = noms_pokemon[i].replace('.png', '')  # Enlever l'extension .png
                            print(f"Vous avez choisi {pokemon_nom} pour commencer la partie")
                            self.pokemon_selectionne = noms_pokemon[i]  # Store the selected Pokemon's name
                            return "interface"

            # Mise à jour de l'affichage de l'interface
            self.ecran.fill((255, 255, 255))
            self.ecran.blit(fond, (0, 0))
            self.ecran.blit(titre, titre_rect)
            for rect, img in zip(pokemon_rects, images_pokemon):
                self.ecran.blit(img, rect)
            if self.pokemon_selectionne is not None:
                pygame.draw.rect(self.ecran, color_active, self.pokemon_selectionne, 2)

            pygame.display.flip()
            # Limitation de la vitesse de la boucle à 30 images par seconde
            pygame.time.Clock().tick(30)
            
        return "interface"
