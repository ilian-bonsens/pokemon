# Importation des modules et des classes nécessaires
import pygame
from menu import Menu
from personnage import Personnage
from fenetre import Fenetre
from choixpokemon import ChoixPokemon
from ajouterpokemon import AjouterPokemon
from interface import Interface
from pokedex import Pokedex  # Assurez-vous d'importer la classe Pokedex

# Définition de la classe Jeu
class Jeu:
    def __init__(self):
        # Initialisation de pygame, du mixeur audio et de la police
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()

        # Création d'une instance de la classe Fenetre
        self.fenetre = Fenetre()

        # Définition de l'état initial du jeu
        self.etat = "menu"

        # Création d'une instance de la classe Pokedex
        self.pokedex = Pokedex('pokedex.json')  # Initialisez le Pokedex ici

    # Méthode pour exécuter le jeu
    def run(self):
        # Boucle principale du jeu
        while True:
            # Si l'état du jeu est "menu", on crée une instance de la classe Menu et on exécute son menu
            if self.etat == "menu":
                menu = Menu(self.fenetre.ecran)
                self.etat = menu.run()

            # Si l'état du jeu est "personnage", on crée une instance de la classe Personnage et on exécute son personnage
            elif self.etat == "personnage":
                personnage = Personnage(self.fenetre.ecran)
                self.etat = personnage.run()

            # Si l'état du jeu est "choixpokemon", on crée une instance de la classe ChoixPokemon et on exécute son choix de pokemon
            elif self.etat == "choixpokemon":
                choix_pokemon = ChoixPokemon(self.fenetre.ecran)
                self.etat = choix_pokemon.run()

            # Si l'état du jeu est "ajouterpokemon", on crée une instance de la classe AjouterPokemon et on exécute son ajout de pokemon
            elif self.etat == "ajouterpokemon":
                ajouter_pokemon = AjouterPokemon()
                self.etat = ajouter_pokemon.run()

            # Si l'état du jeu est "interface", on crée une instance de la classe Interface et on exécute son interface
            elif self.etat == "interface":
                interface = Interface(self.fenetre, 300, 300, 400, 400, 'pokedex.json')
                self.etat = interface.run()

            # Si l'état du jeu est "pokedex", on exécute le pokedex et on revient au menu
            elif self.etat == "pokedex":
                self.pokedex.run(self.fenetre.ecran)
                self.etat = "menu"

            # Si l'état du jeu est "quitter", on sort de la boucle principale
            elif self.etat == "quitter":
                break

            # Mise à jour de l'affichage
            pygame.display.flip()

            # Limitation du nombre d'images par seconde à 60
            pygame.time.Clock().tick(60)

        # Quitter pygame une fois que la boucle principale est terminée
        pygame.quit()

# Si ce fichier est le fichier principal, on crée une instance de la classe Jeu et on exécute le jeu
if __name__ == "__main__":
    jeu = Jeu()
    jeu.run()
