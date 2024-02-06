import pygame
from menu import Menu
from personnage import Personnage
from fenetre import Fenetre
from choixpokemon import ChoixPokemon
from ajouterpokemon import AjouterPokemon
from interface import Interface
from pokedex import Pokedex  # Assurez-vous d'importer la classe Pokedex

class Jeu:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()
        self.fenetre = Fenetre()
        self.etat = "menu"
        self.pokedex = Pokedex('pokedex.json')  # Initialisez le Pokedex ici

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
            elif self.etat == "pokedex":
                self.pokedex.run(self.fenetre.ecran)
                self.etat = "menu"
            elif self.etat == "quitter":
                break
            pygame.display.flip()
            pygame.time.Clock().tick(60)

        pygame.quit()

if __name__ == "__main__":
    jeu = Jeu()
    jeu.run()
