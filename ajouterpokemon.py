import pygame
import sys # Importe le module sys nécessaire pour quitter le jeu

class AjouterPokemon:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 500))
        self.screen.fill((255, 255, 255)) 
        # Charge les images des Pokémon à partir du dossier "imagesM" et les stocke dans une liste
        self.pokemon_images = [pygame.image.load(f'imagesM/{name}.png') for name in ['arbok', 'empiflor', 'Grodoudou', 'kadabra', 'mélodelfe', 'nidorina', 'papillusion', 'Raflesia', 'rattata', 'Roucoups', 'sabelette', 'saquedeneu']]
        self.selected_pokemon = None # Aucun Pokémon n'est sélectionné au début

    def draw_grid(self):
        # Calcule la largeur, la hauteur, et les espacements entre les images pour aligner dans une grille
        image_width = self.pokemon_images[0].get_width()
        image_height = self.pokemon_images[0].get_height()
        gap_x = (800 - 4 * image_width) / 5
        gap_y = (500 - 3 * image_height) / 4

        for i in range(3):
            for j in range(4):
                img_index = i * 4 + j
                img_x = gap_x + j * (image_width + gap_x)
                img_y = gap_y + i * (image_height + gap_y)
                self.screen.blit(self.pokemon_images[img_index], (img_x, img_y))

                # Dessiner un contour vert si cette image est sélectionnée
                if self.selected_pokemon == img_index:
                    pygame.draw.rect(self.screen, (0, 255, 0), (img_x, img_y, image_width, image_height), 3)

    def run(self):
        while True: # Boucle infinie pour garder le jeu en marche
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # Si l'utilisateur ferme la fenêtre
                    pygame.quit()
                    sys.exit() # Ferme le programme
                elif event.type == pygame.MOUSEBUTTONDOWN: # Si l'utilisateur clique sur la souris
                    x, y = pygame.mouse.get_pos()
                    self.selected_pokemon = self.get_pokemon_at_pos(x, y)
                    if self.selected_pokemon is not None: # Si un Pokémon est sélectionné
                        pokemon_name = ['arbok', 'empiflor', 'Grodoudou', 'kadabra', 'mélodelfe', 'nidorina', 'papillusion', 'Raflesia', 'rattata', 'Roucoups', 'sabelette', 'saquedeneu'][self.selected_pokemon]
                        print(f"Le pokémon {pokemon_name} est ajouté.")
                        return "menu"

            self.draw_grid() # Redessine la grille et les Pokémon à chaque itération
            pygame.display.update()

    def get_pokemon_at_pos(self, x, y):
        # Calcule à nouveau la grille pour trouver quelle image a été cliquée
        image_width = self.pokemon_images[0].get_width()
        image_height = self.pokemon_images[0].get_height()
        gap_x = (800 - 4 * image_width) / 5
        gap_y = (500 - 3 * image_height) / 4

        for i in range(3):
            for j in range(4):
                img_x = gap_x + j * (image_width + gap_x)
                img_y = gap_y + i * (image_height + gap_y)

                if img_x <= x <= img_x + image_width and img_y <= y <= img_y + image_height:
                    return i * 4 + j  # Retourne l'index de l'image cliquée
        return None # Si aucun Pokémon n'est cliqué, retourne None

if __name__ == "__main__":
    jeu = AjouterPokemon() # Crée une instance de la classe
    jeu.run() # Exécute la boucle principale du jeu



