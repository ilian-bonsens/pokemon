import pygame
from fenetre import Fenetre
from menu import Menu

pygame.init()

class Personnage:
    def __init__(self):
        self.fenetre = Fenetre()

    def run(self):
        taille_fenetre = (800, 600)
        fenetre = pygame.display.set_mode(taille_fenetre)
        fond = pygame.image.load('images/img10.png')

        largeur_image, hauteur_image = fond.get_size()
        nouvelle_hauteur = int(taille_fenetre[0] * hauteur_image / largeur_image)
        fond = pygame.transform.scale(fond, (taille_fenetre[0], nouvelle_hauteur))

        pygame.mixer.music.load('musique/musique1.mp3')
        pygame.mixer.music.play(-1)

        titre = pygame.image.load('images/titre1.png')
        titre = pygame.transform.scale(titre, (titre.get_width() // 2, titre.get_height() // 2))
        titre_rect = titre.get_rect(center=(taille_fenetre[0] // 2, taille_fenetre[1] // 2 - 210))

        input_box = pygame.Rect(taille_fenetre[0] // 2 - 130, taille_fenetre[1] // 2 + 80, 260, 30)

        police = pygame.font.Font('font/PokemonClassic.ttf', 13)

        texte = police.render("Rentre le nom de ton personnage et clique sur son avatar", True, (255, 255, 255))
        texte_rect = texte.get_rect()
        texte_rect.centerx = taille_fenetre[0] // 2
        texte_rect.bottom = input_box.top - 10

        fille = Personnage('fille', 'images/perso1.png')
        fille.image = pygame.transform.scale(fille.image, (int(fille.image.get_width() * 0.45),
                                                            int(fille.image.get_height() * 0.45)))

        garcon = Personnage('garcon', 'images/perso2.png')
        garcon.image = pygame.transform.scale(garcon.image, (int(garcon.image.get_width() * 0.45),
                                                              int(garcon.image.get_height() * 0.45)))

        largeur_fenetre = taille_fenetre[0]
        largeur_image_fille = fille.image.get_width()
        largeur_image_garcon = garcon.image.get_width()
        espace = (largeur_fenetre - largeur_image_fille - largeur_image_garcon) / 3

        fille_rect = fille.image.get_rect(center=(espace + largeur_image_fille / 2, taille_fenetre[1] // 2 - 65))
        garcon_rect = garcon.image.get_rect(center=(2 * espace + largeur_image_fille + largeur_image_garcon / 2,
                                                   taille_fenetre[1] // 2 - 65))

        color_inactive = pygame.Color('black')
        color_active = pygame.Color('lightgreen')
        color_texte_utilisateur = pygame.Color('white')

        active = False
        text = ''
        font = pygame.font.Font('font/PokemonClassic.ttf', 13)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if input_box.collidepoint(x, y):
                        active = not active
                    else:
                        active = False
                    color = color_active if active else color_inactive
                elif event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            print(text)
                            text = ''
                            menu = Menu()
                            menu.run()
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            fenetre.fill((255, 255, 255))
            fenetre.blit(fond, (0, 0))
            fenetre.blit(titre, titre_rect)
            fenetre.blit(texte, texte_rect)
            fenetre.blit(fille.image, fille_rect)
            fenetre.blit(garcon.image, garcon_rect)
            pygame.draw.rect(fenetre, color_inactive, input_box)
            txt_surface = font.render(text, True, color_texte_utilisateur)
            txt_rect = txt_surface.get_rect()
            txt_rect.center = input_box.center
            fenetre.blit(txt_surface, txt_rect.topleft)
            pygame.display.flip()
            pygame.time.Clock().tick(30)

# Code pour la classe PokemonChoix (actuellement vide, à compléter si nécessaire)
class PokemonChoix:
    def __init__(self):
        pass
