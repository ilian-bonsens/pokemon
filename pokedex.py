import pygame
import json
import os

class Pokedex:
    def __init__(self, json_file):
        with open(json_file, 'r') as f:
            self.pokedex = json.load(f)
        self.sprites = {}
        self.type_images = {}  # Nouveau dictionnaire pour stocker les images de type
        for name, pokemon in self.pokedex.items():
            self.sprites[name] = pygame.image.load(pokemon['sprite-face'])
            if 'type' in pokemon and isinstance(pokemon['type'], str) and os.path.isfile(pokemon['type']):  # Vérifiez si le fichier existe
                self.type_images[name] = pygame.image.load(pokemon['type'])  # Charger l'image du type à partir de la clé 'type'

    def get_pokemon(self, name):
        return self.pokedex.get(name, None)

    def get_sprite(self, name):
        return self.sprites.get(name, None)

    def get_type_image(self, name):  # Nouvelle méthode pour obtenir l'image du type
        return self.type_images.get(name, None)

# Initialiser Pygame
pygame.init()

# Définir la taille de la fenêtre
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

# Charger l'image de fond et la redimensionner pour qu'elle corresponde à la taille de la fenêtre
background = pygame.image.load('image-l/pokedex.png')
background = pygame.transform.scale(background, window_size)

# Charger les données du Pokedex
pokedex = Pokedex('pokedex.json')

# Créer une police pour afficher les statistiques
font = pygame.font.Font(None, 36)

# Boucle principale
running = True
selected_pokemon = None
pokemon_names = list(pokedex.pokedex.keys())
pokemon_index = 0
while running:
    # Dessiner l'image de fond
    screen.blit(background, (0, 0))

    # Dessiner le sprite du Pokémon sélectionné
    sprite = pokedex.get_sprite(pokemon_names[pokemon_index])
    if sprite is not None:
        # Doubler la taille du sprite pour tous les Pokémon sauf Pikachu
        if pokemon_names[pokemon_index] == 'Pikachu':
            sprite = pygame.transform.scale(sprite, (96, 96))
            # Dessiner Pikachu à des coordonnées spécifiques
            screen.blit(sprite, (120, 120))  # Ajustez ces valeurs comme vous le souhaitez
        else:
            sprite = pygame.transform.scale(sprite, (sprite.get_width() * 2, sprite.get_height() * 2))
            # Dessiner les autres Pokémon légèrement à droite et en bas
            screen.blit(sprite, (70, 60))  # Ajustez ces valeurs comme vous le souhaitez

    # Afficher les statistiques du Pokémon sélectionné
    stats = pokedex.get_pokemon(pokemon_names[pokemon_index])
    if stats is not None:
        type_image = pokedex.get_type_image(pokemon_names[pokemon_index])  # Obtenir l'image du type
        if type_image is not None:
            screen.blit(type_image, (450, 170))  # Afficher l'image du type

        attack_info = ', '.join([attack['name'] for attack in stats['attacks']])
        info_list = [
            f"HP: {stats['hp']}",
            f"Atk: {stats['attack']}",
            f"Def: {stats['defense']}",
            f"Spd: {stats['speed']}",
            f"Attacks: {attack_info}"
        ]
        for i, info in enumerate(info_list):
            text = font.render(info, True, (0, 0, 0))
            screen.blit(text, (window_size[0] // 2, window_size[1] // 2 + i * 40))

    # Mettre à jour l'écran
    pygame.display.flip()

    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pokemon_index = (pokemon_index - 1) % len(pokemon_names)
            elif event.key == pygame.K_DOWN:
                pokemon_index = (pokemon_index + 1) % len(pokemon_names)

# Quitter Pygame
pygame.quit()
