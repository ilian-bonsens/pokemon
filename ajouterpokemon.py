import pygame
import sys

class AjouterPokemon:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 500))
        self.screen.fill((255, 255, 255))  # Fond blanc
        self.pokemon_images = [pygame.image.load(f'imagesM/{name}.png') for name in ['arbok', 'empiflor', 'Grodoudou', 'kadabra', 'mélodelfe', 'nidorina', 'papillusion', 'Raflesia', 'rattata', 'Roucoups', 'sabelette', 'saquedeneu']]
        self.selected_pokemon = None

    def draw_grid(self):
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
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    self.selected_pokemon = self.get_pokemon_at_pos(x, y)
                    if self.selected_pokemon is not None:
                        pokemon_name = ['arbok', 'empiflor', 'Grodoudou', 'kadabra', 'mélodelfe', 'nidorina', 'papillusion', 'Raflesia', 'rattata', 'Roucoups', 'sabelette', 'saquedeneu'][self.selected_pokemon]
                        print(f"Le pokémon {pokemon_name} est ajouté.")
                        return "menu"

            self.draw_grid()
            pygame.display.update()

    def get_pokemon_at_pos(self, x, y):
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
        return None

if __name__ == "__main__":
    jeu = AjouterPokemon()
    jeu.run()



