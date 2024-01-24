import pygame
import json

class Pokedex:
    def __init__(self, json_file):
        with open(json_file, 'r') as f:
            self.pokedex = json.load(f)
        self.sprites = {}
        for name, pokemon in self.pokedex.items():
            self.sprites[name] = pygame.image.load(pokemon['sprite-face'])

    def get_pokemon(self, name):
        return self.pokedex.get(name, None)

    def get_sprite(self, name):
        return self.sprites.get(name, None)

# Initialiser Pygame
pygame.init()

# Définir la taille de la fenêtre
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

# Charger les données du Pokedex
pokedex = Pokedex('pokedex.json')

# Créer une police pour afficher les statistiques
font = pygame.font.Font(None, 36)

# Boucle principale
running = True
selected_pokemon = None
while running:
    # Remplir l'écran avec une couleur
    screen.fill((255, 255, 255))

    # Dessiner les sprites des Pokémon
    for i, (name, pokemon) in enumerate(pokedex.pokedex.items()):
        sprite = pokedex.get_sprite(name)
        if sprite is not None:
            screen.blit(sprite, (i * 64, 0))

    # Afficher les statistiques du Pokémon sélectionné
    if selected_pokemon is not None:
        stats = pokedex.get_pokemon(selected_pokemon)
        if stats is not None:
            type_info = ', '.join(stats['type']) if isinstance(stats['type'], list) else stats['type']
            attack_info = ', '.join([attack['name'] for attack in stats['attacks']])
            info_list = [
                f"Type: {type_info}",
                f"HP: {stats['hp']}",
                f"Atk: {stats['attack']}",
                f"Def: {stats['defense']}",
                f"Spd: {stats['speed']}",
                f"Attacks: {attack_info}"
            ]
            for i, info in enumerate(info_list):
                text = font.render(info, True, (0, 0, 0))
                screen.blit(text, (10, window_size[1] - (len(info_list) - i) * 40))

    # Mettre à jour l'écran
    pygame.display.flip()

    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            selected_pokemon = None
            for i, (name, pokemon) in enumerate(pokedex.pokedex.items()):
                sprite = pokedex.get_sprite(name)
                if sprite is not None and i * 64 <= x < (i + 1) * 64 and 0 <= y < 64:
                    selected_pokemon = name
                    break

# Quitter Pygame
pygame.quit()
