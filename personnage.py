import pygame

class Personnage:
    def __init__(self, ecran):
        self.ecran = ecran
        self.nom = None
        self.image_path = None
        self.image = None
        self.personnage_selectionne = None # Variable pour suivre le personnage sélectionné

    def run(self):         
        taille_fenetre = (800, 600)
        fond = pygame.image.load('imagesM/img11.png')
        fond = pygame.transform.scale(fond, taille_fenetre)

        pygame.mixer.music.load('musiqueM/Pokemonmusic1.mp3')
        pygame.mixer.music.play(-1)

        # Chargement de l'image du titre et redimensionnement
        titre = pygame.image.load('imagesM/txt2.png')
        rapport = 550 / titre.get_width()  # Nouvelle largeur de 200 pixels
        nouvelle_hauteur = int(titre.get_height() * rapport)
        titre = pygame.transform.scale(titre, (550, nouvelle_hauteur))
        titre_rect = titre.get_rect(center=(taille_fenetre[0] // 2, taille_fenetre[1] // 2 - 210))

        # Chargement et redimensionnement des images des personnages
        image_fille = pygame.image.load('imagesM/prof1.png')
        image_garcon = pygame.image.load('imagesM/prof2.png')
        # Calcul du rapport de redimensionnement pour conserver les proportions
        rapport_fille = 200 / image_fille.get_height()
        rapport_garcon = 200 / image_garcon.get_height()
        # Application du rapport pour obtenir la nouvelle largeur tout en conservant les proportions
        nouvelle_largeur_fille = int(image_fille.get_width() * rapport_fille)
        nouvelle_largeur_garcon = int(image_garcon.get_width() * rapport_garcon)
        # Redimensionnement des images
        image_fille = pygame.transform.scale(image_fille, (nouvelle_largeur_fille, 200))
        image_garcon = pygame.transform.scale(image_garcon, (nouvelle_largeur_garcon, 200)) 

        # Calcul des positions pour les images de personnages
        espacement = 40  # Espacement entre les images et le centre
        centre_x = taille_fenetre[0] // 2
        decalage_vertical = 55
        fille_rect = image_fille.get_rect(center=(centre_x - espacement - image_fille.get_width() // 2, taille_fenetre[1] // 2 - decalage_vertical))
        garcon_rect = image_garcon.get_rect(center=(centre_x + espacement + image_garcon.get_width() // 2, taille_fenetre[1] // 2 - decalage_vertical))

        # Initialisation de la zone de saisie de texte
        color_inactive = pygame.Color('black')
        color_active = pygame.Color('lightgreen')
        color_texte_utilisateur = pygame.Color('white')
        active = False
        text = ''
        font = pygame.font.Font('fontM/PokemonClassic.ttf', 13)
        # Définition de la largeur et de la hauteur de la zone de saisie
        input_box_width = 380
        input_box_height = 32
        # Calcul de la position x pour centrer la zone de saisie
        input_box_x = (taille_fenetre[0] - input_box_width) // 2
        input_box_y = 350 + 30
        input_box = pygame.Rect(input_box_x, input_box_y, input_box_width, input_box_height)

        # Boucle principale
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quitter"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Gestion de la sélection de la zone de texte
                    if input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    
                    x, y = pygame.mouse.get_pos()
                    if fille_rect.collidepoint(x, y):
                        self.nom = 'fille'
                        self.image_path = 'imagesM/perso1.png'
                        self.image = image_fille
                        self.personnage_selectionne = 'fille'
                        self.personnage_selectionne = fille_rect  # Enregistrez le rectangle de l'image sélectionnée
                    elif garcon_rect.collidepoint(x, y):
                        self.nom = 'garcon'
                        self.image_path = 'imagesM/perso2.png'
                        self.image = image_garcon
                        self.personnage_selectionne = 'garcon'
                        self.personnage_selectionne = garcon_rect
                    else:
                        color_inactive = pygame.Color('black') if not active else color_active

                elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            print(f"Bienvenue dans la partie {text} !")
                            return "choixpokemon" # Retourne un nouveau statut lorsqu'Entrée est pressée
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            # Affichage des éléments graphiques
            self.ecran.fill((255, 255, 255))
            self.ecran.blit(fond, (0, 0))
            self.ecran.blit(titre, titre_rect)
            self.ecran.blit(image_fille, fille_rect)
            self.ecran.blit(image_garcon, garcon_rect)

            # Calcul de la largeur du texte
            txt_surface = font.render(text, True, color_texte_utilisateur)
            text_width, text_height = txt_surface.get_size()
            # Calcul de la position x pour centrer le texte dans la zone de saisie
            text_x = input_box.x + (input_box.width - text_width) // 2
            text_y = input_box.y + (input_box.height - text_height) // 2
            # Remplissage de la zone de saisie avec la couleur noire
            pygame.draw.rect(self.ecran, pygame.Color('black'), input_box)
            # Dessin du contour de la zone de saisie
            pygame.draw.rect(self.ecran, color_inactive, input_box, 2)
            # Affichage du texte centré
            self.ecran.blit(txt_surface, (text_x, text_y))
            
            if self.personnage_selectionne is not None:
                pygame.draw.rect(self.ecran, color_active, self.personnage_selectionne, 2)
            

            pygame.display.flip()
            pygame.time.Clock().tick(30)
            
        return "quitter"


   

            

