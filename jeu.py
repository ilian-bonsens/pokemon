import pygame
from menu import Menu
from personnage import Personnage
from fenetre import Fenetre
from choixpokemon import ChoixPokemon
from ajouterpokemon import AjouterPokemon

class Jeu:
    def __init__(self):
        self.fenetre = Fenetre()
        self.etat = "menu"

    def run(self):
        while True:
            if self.etat == "menu":
                menu = Menu(self.fenetre.ecran)
                self.etat = menu.run()  # Exécute le menu et récupère le prochain état
            elif self.etat == "personnage":
                personnage = Personnage(self.fenetre.ecran)
                self.etat = personnage.run()  # Exécute la sélection de personnage
            elif self.etat == "choixpokemon":
                choix_pokemon = ChoixPokemon(self.fenetre.ecran)
                self.etat = choix_pokemon.run()  # Exécute la sélection de Pokemon
            elif self.etat == "ajouterpokemon":  # Nouvel état
                ajouter_pokemon = AjouterPokemon()
                self.etat = ajouter_pokemon.run()
            elif self.etat == "quitter":
                break  # Sortie de la boucle si l'état est 'quitter'

            pygame.display.flip()
            pygame.time.Clock().tick(self.fenetre.framerate)

        pygame.quit()

# Exécuter le jeu
if __name__ == "__main__":
    pygame.init()
    pygame.font.init()  # Assurez-vous que cette ligne est présente
    jeu = Jeu()
    jeu.run()
