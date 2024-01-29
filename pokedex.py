import pygame
import json
import os
import pygame.mixer

# Initialiser le mixer
pygame.mixer.init()


class Pokedex:
    def __init__(self, json_file):
        # Définir la taille de la fenêtre
        self.window_size = (800, 600)

        with open(json_file, 'r') as f:
            self.pokedex = json.load(f)
        self.sprites = {}
        self.type_images = {}
        self.cris = {}
        for name, pokemon in self.pokedex.items():
            self.sprites[name] = pygame.image.load(pokemon['sprite-face'])
            if 'type' in pokemon and isinstance(pokemon['type'], str) and os.path.isfile(pokemon['type']):
                image = pygame.image.load(pokemon['type'])
                width = int(image.get_width() * 0.7)
                height = int(image.get_height() * 0.7)
                self.type_images[name] = pygame.transform.scale(image, (width, height))
            cri_path = os.path.join('cri-pokemon', f'{name}.ogg')
            if os.path.isfile(cri_path):
                self.cris[name] = pygame.mixer.Sound(cri_path)
        self.hp_coords = (100, 435)
        self.atk_coords = (100, 465)
        self.def_coords = (100, 495)
        self.spd_coords = (100, 525)
        self.name_coords = (400, 80)
        self.attacks_coords = [(350, 431 + i * int(0.05 * self.window_size[1])) for i in range(4)]
        self.id_coords = (350, 230)

    def get_pokemon(self, name):
        return self.pokedex.get(name, None)

    def get_sprite(self, name):
        return self.sprites.get(name, None)

    def get_type_image(self, name):
        return self.type_images.get(name, None)

    def get_cri(self, name):
        return self.cris.get(name, None)

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode(self.window_size)
        background = pygame.image.load('image-l/pokedex.png')
        background = pygame.transform.scale(background, self.window_size)
        font_path = os.path.join('fonts', 'PokemonClassic.ttf')
        font_size = 15
        font = pygame.font.Font(font_path, font_size)
        running = True
        selected_pokemon = None
        pokemon_names = list(self.pokedex.keys())
        pokemon_index = 0
        last_pokemon_index = None
        while running:
            screen.blit(background, (0, 0))
            sprite = self.get_sprite(pokemon_names[pokemon_index])
            if sprite is not None:
                if pokemon_names[pokemon_index] == 'Pikachu':
                    sprite = pygame.transform.scale(sprite, (96, 96))
                    screen.blit(sprite, (120, 150))
                else:
                    sprite = pygame.transform.scale(sprite, (sprite.get_width() * 2, sprite.get_height() * 2))
                    screen.blit(sprite, (70, 90))
            name_text = font.render(pokemon_names[pokemon_index], True, (0, 0, 0))
            screen.blit(name_text, self.name_coords)
            stats = self.get_pokemon(pokemon_names[pokemon_index])
            if stats is not None:
                type_image = self.get_type_image(pokemon_names[pokemon_index])
                if type_image is not None:
                    screen.blit(type_image, (480, 271))
                attack_info = [attack['name'] for attack in stats['attacks']]
                info_list = [
                    (f"HP: {stats['hp']}", self.hp_coords),
                    (f"Atk: {stats['attack']}", self.atk_coords),
                    (f"Def: {stats['defense']}", self.def_coords),
                    (f"Spd: {stats['speed']}", self.spd_coords),
                ]
                for i, attack in enumerate(attack_info):
                    info_list.append((f"Attack {i + 1}: {attack}", self.attacks_coords[i]))
                for info, coords in info_list:
                    text = font.render(info, True, (0, 0, 0))
                    screen.blit(text, coords)
                id_text = font.render(str(stats['id']), True, (0, 0, 0))
                screen.blit(id_text, self.id_coords)
            if pokemon_index != last_pokemon_index:
                cri = self.get_cri(pokemon_names[pokemon_index])
                if cri is not None:
                    cri.play()
                last_pokemon_index = pokemon_index
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        pokemon_index = (pokemon_index - 1) % len(pokemon_names)
                    elif event.key == pygame.K_DOWN:
                        pokemon_index = (pokemon_index + 1) % len(pokemon_names)
        pygame.quit()


pokedex = Pokedex('pokedex.json')
pokedex.run()
