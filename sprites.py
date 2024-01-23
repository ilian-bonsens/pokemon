import json, pygame, random
from fenetre import Fenetre

pygame.init()

fenetre = Fenetre()

class Sprites:
    def __init__(self, x, y, x2, y2, json_file):
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2

        with open(json_file, 'r', encoding='utf-8') as f:
            self.json = json.load(f)

        self.set_sprite1("Pikachu", "sprite-dos")
        self.random_pokemon = random.choice([name for name in self.json.keys() if name != "Pikachu" and "sprite-face" in self.json[name]])
        self.set_sprite2(self.random_pokemon, "sprite-face")
        self.cri()

    def set_sprite1(self, pokemon_name, sprite_type):
        # Récupérer le chemin du sprite
        sprite_path = self.json[pokemon_name][sprite_type]

        # Charger le sprite
        self.image = pygame.image.load(sprite_path).convert_alpha()

        # Définir les nouvelles dimensions
        new_width = self.image.get_width() * 3 # Multiplier par 3 pour tripler la taille
        new_height = self.image.get_height() * 3  # Multiplier par 3 pour tripler la taille

        # Redimensionner l'image tout en conservant les proportions
        self.image = pygame.transform.scale(self.image, (new_width, new_height))

    def set_sprite2(self, pokemon_name, sprite_type):
        # Récupérer le chemin du sprite
        sprite_path = self.json[pokemon_name][sprite_type]

        # Charger le sprite
        self.image2 = pygame.image.load(sprite_path).convert_alpha()

        # Définir les nouvelles dimensions
        new_width2 = self.image2.get_width() * 2  # Multiplier par 2.5 pour augmenter la taille
        new_height2 = self.image2.get_height() * 2 # Multiplier par 2.5 pour augmenter la taille

        # Redimensionner l'image tout en conservant les proportions
        self.image2 = pygame.transform.scale(self.image2, (new_width2, new_height2))

    def draw(self):
        # Calculer la position pour centrer le sprite
        x = self.json["Pikachu"]["axe x"]
        y = self.json["Pikachu"]["axe y"]

        # Dessiner le sprite
        sprite = self.image.copy()
        transparency = (255, 255, 255, 255)
        sprite.fill(transparency, None, pygame.BLEND_RGBA_MULT)
        fenetre.ecran.blit(sprite, (x, y))

    def draw2(self):
        # Calculer la position pour centrer le sprite en face
        x2 = self.json[self.random_pokemon]["axe x2"]
        y2 = self.json[self.random_pokemon]["axe y2"]

        # Dessiner le sprite
        sprite = self.image2.copy()
        transparency = (255, 255, 255, 255)
        sprite.fill(transparency, None, pygame.BLEND_RGBA_MULT)
        fenetre.ecran.blit(sprite, (x2, y2))

    def cri(self):
        pygame.mixer.music.load(self.json["Pikachu"]["cri"])
        pygame.mixer.music.play()

        # Mettre en file d'attente le cri du deuxième Pokémon
        pygame.mixer.music.queue(self.json[self.random_pokemon]["cri"])

        # Attendre 0.5 secondes avant de commencer à jouer le cri du deuxième Pokémon
        pygame.time.wait(2000)

    