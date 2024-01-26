import pygame
import json
import os
import pygame.mixer

class Pokedex:
    def __init__(self, json_file):
        with open(json_file, 'r') as f:
            self.pokedex = json.load(f)
        self.sprites = {}
        self.type_images = {}  # Nouveau dictionnaire pour stocker les images de type
        self.cris = {}  # Nouveau dictionnaire pour stocker les cris de chaque Pokémon
        for name, pokemon in self.pokedex.items():
            self.sprites[name] = pygame.image.load(pokemon['sprite-face'])
            if 'type' in pokemon and isinstance(pokemon['type'], str) and os.path.isfile(pokemon['type']):  # Vérifiez si le fichier existe
                image = pygame.image.load(pokemon['type'])  # Charger l'image du type à partir de la clé 'type'
                # Réduire la taille de l'image de 30%
                width = int(image.get_width() * 0.7)
                height = int(image.get_height() * 0.7)
                self.type_images[name] = pygame.transform.scale(image, (width, height))
            cri_path = os.path.join('cri-pokemon', f'{name}.ogg')  # Assurez-vous que le format du fichier est correct
            if os.path.isfile(cri_path):  # Vérifiez si le fichier existe
                self.cris[name] = pygame.mixer.Sound(cri_path)
        # Définir les coordonnées comme des attributs de la classe
        self.hp_coords = (100, 435)
        self.atk_coords = (100, 465)
        self.def_coords = (100, 495)
        self.spd_coords = (100, 525)
        self.name_coords = (400, 80)  # Ajoutez les coordonnées pour "name"
        self.attacks_coords = [(350, 431 + i*int(0.05 * window_size[1])) for i in range(4)]  # Créez une liste de coordonnées pour chaque attaque
        self.id_coords = (350, 230)  # Ajoutez ceci pour définir les coordonnées de l'ID

    def get_pokemon(self, name):
        return self.pokedex.get(name, None)

    def get_sprite(self, name):
        return self.sprites.get(name, None)

    def get_type_image(self, name):  # Nouvelle méthode pour obtenir l'image du type
        return self.type_images.get(name, None)

    def get_cri(self, name):  # Nouvelle méthode pour obtenir le cri d'un Pokémon
        return self.cris.get(name, None)

# Initialiser Pygame
pygame.init()

# Initialiser le mixer
pygame.mixer.init()

# Définir la taille de la fenêtre
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

# Charger l'image de fond et la redimensionner pour qu'elle corresponde à la taille de la fenêtre
background = pygame.image.load('image-l/pokedex.png')
background = pygame.transform.scale(background, window_size)

# Charger les données du Pokedex
pokedex = Pokedex('pokedex.json')

# Créer une police pour afficher les statistiques
font_path = os.path.join('fonts', 'PokemonClassic.ttf')  # Assurez-vous que le chemin est correct
font_size = 15
font = pygame.font.Font(font_path, font_size)

# Boucle principale
running = True
selected_pokemon = None
pokemon_names = list(pokedex.pokedex.keys())
pokemon_index = 0
last_pokemon_index = None  # Ajouter une variable pour garder une trace du dernier Pokémon sélectionné
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
            screen.blit(sprite, (120, 150))  # Ajustez ces valeurs comme vous le souhaitez
        else:
            sprite = pygame.transform.scale(sprite, (sprite.get_width() * 2, sprite.get_height() * 2))
            # Dessiner les autres Pokémon légèrement à droite et en bas
            screen.blit(sprite, (70, 90))  # Ajustez ces valeurs comme vous le souhaitez

    # Afficher le nom du Pokémon sélectionné
    name_text = font.render(pokemon_names[pokemon_index], True, (0, 0, 0))
    screen.blit(name_text, pokedex.name_coords)  # Utilisez les nouvelles coordonnées pour "name"

    # Afficher les statistiques du Pokémon sélectionné
    stats = pokedex.get_pokemon(pokemon_names[pokemon_index])
    if stats is not None:
        type_image = pokedex.get_type_image(pokemon_names[pokemon_index])  # Obtenir l'image du type
        if type_image is not None:
            screen.blit(type_image, (480, 271))  # Afficher l'image du type

        attack_info = [attack['name'] for attack in stats['attacks']]
        info_list = [
            (f"HP: {stats['hp']}", pokedex.hp_coords),
            (f"Atk: {stats['attack']}", pokedex.atk_coords),
            (f"Def: {stats['defense']}", pokedex.def_coords),
            (f"Spd: {stats['speed']}", pokedex.spd_coords),
        ]
        for i, attack in enumerate(attack_info):
            info_list.append((f"Attack {i+1}: {attack}", pokedex.attacks_coords[i]))  # Utilisez une coordonnée différente pour chaque attaque
        for info, coords in info_list:
            text = font.render(info, True, (0, 0, 0))
            screen.blit(text, coords)

        id_text = font.render(str(stats['id']), True, (0, 0, 0))  # Créez un texte avec l'ID du Pokémon
        screen.blit(id_text, pokedex.id_coords)  # Affichez l'ID aux coordonnées spécifiées

    # Jouer le cri du Pokémon sélectionné seulement s'il a changé
    if pokemon_index != last_pokemon_index:
        cri = pokedex.get_cri(pokemon_names[pokemon_index])
        if cri is not None:
            cri.play()
        last_pokemon_index = pokemon_index  # Mettre à jour le dernier Pokémon sélectionné

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

# Quitter
pygame.quit()
