import pygame, json, random
from fenetre import Fenetre

pygame.init()
pygame.mixer.init()

fenetre = Fenetre()

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 200, 0)
red = (200, 0, 0)
dark_grey = (50, 50, 50)
light_grey = (150, 150, 150)
yellow = (222, 193, 96)

class Combat:
    def __init__(self, x, y, x2, y2, json_file):
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2

        with open(json_file, 'r', encoding='utf-8') as f:
            self.json = json.load(f)

        # Charger les sprites
        self.set_sprite1("Tortank", "sprite-dos")
        self.random_pokemon = random.choice([name for name in self.json.keys() if name != "Tortank" and "sprite-face" in self.json[name]])
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
        x = self.json["Tortank"]["axe x"]
        y = self.json["Tortank"]["axe y"]

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

    def draw_pv(self):
        pygame.draw.rect(fenetre.ecran, green, (450, 70, 170, 8))
        pygame.draw.rect(fenetre.ecran, green, (50, 180, 170, 8))

    def cri(self):
        pygame.mixer.music.load(self.json["Tortank"]["cri"])
        pygame.mixer.music.play()

        # Mettre en file d'attente le cri du deuxième Pokémon
        pygame.mixer.music.queue(self.json[self.random_pokemon]["cri"])

        # Attendre 0.5 secondes avant de commencer à jouer le cri du deuxième Pokémon
        pygame.time.wait(2000)

    def interface(self):
        # Charger l'image d'arrière-plan
        background = pygame.image.load("images/Battle-Backgrounds.png").convert_alpha()

        # Redimensionner l'image d'arrière-plan pour qu'elle ait la même largeur que le rectangle
        background = pygame.transform.scale(background, (800, int(660 * background.get_height() / background.get_width())))

        # Dessiner l'image d'arrière-plan par-dessus le rectangle
        fenetre.ecran.blit(background, (0, 0))

        self.draw()
        self.draw2()
        self.draw_pv()

        # Dessine le rectangle gris en fond
        pygame.draw.rect(fenetre.ecran, dark_grey, (0, 370, 800, 130))
        # Dessine à droite le rectangle jaune en premier
        pygame.draw.rect(fenetre.ecran, yellow, (10, 380, 380, 110), 0, 4)
        # Dessine à droite le rectangle blanc par-dessus
        pygame.draw.rect(fenetre.ecran, white, (15, 385, 370, 100), 0, 4)
        # Dessine à gauche le rectangle gris clair par-dessus
        pygame.draw.rect(fenetre.ecran, light_grey, (400, 380, 390, 110), 0, 4)

        pygame.display.flip()
    
    def create_button(width, height, left, top, text_cx, text_cy, label):
        # position of the mouse cursor
        mouse_cursor = pygame.mouse.get_pos()
    
        button = pygame.rect(left, top, width, height)
        
        # highlight the button if mouse is pointing to it
        if button.collidepoint(mouse_cursor):
            pygame.draw.rect(fenetre.ecran, yellow, button)
        else:
            pygame.draw.rect(fenetre.ecran, white, button)
            
        # add the label to the button
        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text = font.render(f'{label}', True, black)
        text_rect = text.get_rect(center=(text_cx, text_cy))
        fenetre.ecran.blit(text, text_rect)
        
        return button

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