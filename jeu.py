import pygame
from menu import Menu
from personnage import Personnage
from fenetre import Fenetre
from choixpokemon import ChoixPokemon
from ajouterpokemon import AjouterPokemon
from interface import Interface




class Jeu:
    def __init__(self):
        self.fenetre = Fenetre()
        self.etat = "menu"

    def run(self):
        while True:
            if self.etat == "menu":
                menu = Menu(self.fenetre.ecran)
                self.etat = menu.run()
            elif self.etat == "personnage":
                personnage = Personnage(self.fenetre.ecran)
                self.etat = personnage.run()
            elif self.etat == "choixpokemon":
                choix_pokemon = ChoixPokemon(self.fenetre.ecran)
                self.etat = choix_pokemon.run()
            elif self.etat == "ajouterpokemon":
                ajouter_pokemon = AjouterPokemon()
                self.etat = ajouter_pokemon.run()
            elif self.etat == "interface":
                interface = Interface(self.fenetre, 300, 300, 400, 400, 'pokedex.json')
                self.etat = interface.run()
            elif self.etat == "quitter":
                break

            pygame.display.flip()
            pygame.time.Clock().tick(self.fenetre.framerate)

        pygame.quit()

# Exécuter le jeu
if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    jeu = Jeu()
    jeu.run()
