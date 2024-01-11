import pygame, json, random, time
from fenetre import Fenetre

pygame.init()
pygame.mixer.init()

fenetre = Fenetre()

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 200, 0)
red = (200, 0, 0)

class Combat:
    def __init__(self, x, y, x2, y2, json_file):
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2

        with open(json_file, 'r', encoding='utf-8') as f:
            self.json = json.load(f)

        # Charger les sprites
        self.set_sprite1("Dracaufeu", "sprite-dos")  # Charger le sprite de dos pour Dracaufeu
        self.set_sprite2(random.choice([name for name in self.json.keys() if name != "Dracaufeu" and "sprite-face" in self.json[name]]), "sprite-face")  # Charger le sprite de face pour le deuxième Pokémon

    def set_sprite1(self, pokemon_name, sprite_type):
        # Récupérer le chemin du sprite
        sprite_path = self.json[pokemon_name][sprite_type]

        # Charger le sprite
        self.image = pygame.image.load(sprite_path).convert_alpha()

        # Définir les nouvelles dimensions
        new_width = self.image.get_width() * 1.7  # Multiplier par 2 pour doubler la taille
        new_height = self.image.get_height() * 1.7  # Multiplier par 2 pour doubler la taille

        # Redimensionner l'image tout en conservant les proportions
        self.image = pygame.transform.scale(self.image, (new_width, new_height))

    def set_sprite2(self, pokemon_name, sprite_type):
        # Récupérer le chemin du sprite
        sprite_path = self.json[pokemon_name][sprite_type]

        # Charger le sprite
        self.image2 = pygame.image.load(sprite_path).convert_alpha()

        # Définir les nouvelles dimensions
        new_width = self.image2.get_width() * 2  # Multiplier par 2.5 pour augmenter la taille
        new_height = self.image2.get_height() * 2  # Multiplier par 2.5 pour augmenter la taille

        # Redimensionner l'image tout en conservant les proportions
        self.image2 = pygame.transform.scale(self.image2, (new_width, new_height))

    def draw(self):
        # Calculer la position pour centrer le sprite
        x = 135
        y = 235

        # Dessiner le sprite
        sprite = self.image.copy()
        transparency = (255, 255, 255, 255)
        sprite.fill(transparency, None, pygame.BLEND_RGBA_MULT)
        fenetre.ecran.blit(sprite, (x, y))

    def draw2(self):
        # Calculer la position pour centrer le sprite
        x2 = 505
        y2 = 90

        # Dessiner le sprite
        sprite = self.image2.copy()
        transparency = (255, 255, 255, 255)
        sprite.fill(transparency, None, pygame.BLEND_RGBA_MULT)
        fenetre.ecran.blit(sprite, (x2, y2))

    def draw_pv(self):
        pygame.draw.rect(fenetre.ecran, green, (450, 70, 170, 8))
        pygame.draw.rect(fenetre.ecran, green, (50, 180, 170, 8))

    def cri(self):
        pygame.mixer.music.load("cris-pokemon/charizard.ogg")
        pygame.mixer.music.play()

    def interface(self):
        # Charger l'image d'arrière-plan
        background = pygame.image.load("images/Backgrounds-4G.png").convert_alpha()

        # Redimensionner l'image d'arrière-plan pour qu'elle ait la même largeur que le rectangle
        background = pygame.transform.scale(background, (800, int(660 * background.get_height() / background.get_width())))

        # Dessiner l'image d'arrière-plan par-dessus le rectangle
        fenetre.ecran.blit(background, (0, 0))

        # Dessiner le rectangle blanc
        pygame.draw.rect(fenetre.ecran, white, (10, 380, 780, 110))

        self.draw()
        self.draw2()
        self.draw_pv()
        self.cri()
        pygame.display.flip()

# Créer une instance de la classe Combat
combat = Combat(300, 300, 400, 400, 'pokedex.json')

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    combat.interface()

pygame.quit()