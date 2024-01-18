import random

class Pokemon:
    def __init__(self, nom, type1, type2, pv, atk, df, atkspe, dfspe, vit, attaque1, attaque2, attaque3, attaque4, combats_gagnes=0):
        self.nom = nom
        self.type1 = type1
        self.type2 = type2
        self.pv = pv
        self.atk = atk
        self.df = df
        self.atkspe = atkspe
        self.dfspe = dfspe
        self.vit = vit
        self.attaque = [attaque1, attaque2, attaque3, attaque4]
        self.combats_gagnes = combats_gagnes
        self.attaques_potentielles = []
        self.evolutions = {"Salamèche": "Reptincel", "Reptincel": "Dracaufeu", "Carapuce": "Carabaffe", "Carabaffe": "Tortank", "Bulbizarre": "Herbizarre", "Herbizarre": "Florizarre"}

    def gagner_combat(self):
        self.combats_gagnes += 1
        if self.combats_gagnes % 4 == 0:  # Si le Pokémon a gagné 4 combats
            self.apprendre_attaque()  # Le Pokémon devrait apprendre une nouvelle attaque
            self.evoluer()  # Le Pokémon devrait évoluer

    def apprendre_attaque(self):
        if self.attaques_potentielles:  # S'il y a des attaques potentielles à apprendre
            self.attaque.append(self.attaques_potentielles.pop(0))  # Apprendre la première attaque potentielle

    def evoluer(self):
        if self.nom in self.evolutions:
            self.nom = self.evolutions[self.nom]
            print(f"Félicitations! Votre {self.nom} a évolué!")
        else:
            print(f"{self.nom} a atteint son évolution finale.")
            self.evolutions.pop(self.nom, None)  # Retirer le Pokémon du dictionnaire des évolutions


class Move:
    def __init__(self, name, form, typ, pwr):
        self.name = name
        self.form = form
        self.typ = typ
        self.pwr = pwr

#Attaque et types
Lanceflamme = Move("Lanceflamme", "Special", "Feu", 90)
Tranche = Move("Tranche", "Physique", "Normal", 70)
Lame_dair = Move("Lame d'Air", "Special", "Vol", 75)
Boutefeu = Move("Boutefeu", "Physique", "Feu", 120)
Hydro_queue = Move("Hydro Queue", "Physique", "Eau", 90)
Vibraqua = Move("Vibraqua", "Special", "Eau", 60)
Morsure = Move("Morsure", "Physique", "Dark", 60)
Tour_rapide = Move("Tour rapide", "Physique", "Normal", 50)
Canon_graine = Move("Canon graine", "Physique", "Plante", 60)
Bombe_Beurk = Move("Bombe Beurk", "Special", "Poison", 90)
Coupe_feuille = Move("Coupe feuille", "Physique", "Plante", 55)
Damoclès = Move("Damoclès", "Physique", "Normal", 120)
Fouet_Lianes = Move("Fouet Lianes", "physique", "plante", 45)
Faux_Coup = Move("Faux_Coup", "physique", "Normal", 40)
Pistolet_a_O = Move("Pistolet_a_O", "Special", "Eau", 40)
Charge = Move("Charge", "Physique", "Normal", 40)
Crocs_Feu = Move("Crocs_Feu", "Physique", "Feu", 65)
Flammeche = Move("Flammeche", "Special", "Feu", 40)
Tranch_Herbe = Move("Tranch_Herbe", "physique", "plante", 95)
Tempête_Florale = Move("Tempête_Florale", "Physique", "plante", 90)
Lance_Soleil = Move("Lance_Soleil", "Special", "plante", 120)
Griffe = Move("Griffe", "physique", "Normal", 40)
Hydrocanon = Move("Hydrocanon", "special", "Eau", 120)
Éclair = Move("Éclair", "special", "Electrik", 40)
Vive_Attaque = Move("Vive_Attaque", "physique", "Normal", 40)
Frotte_Frimousse = Move("Frotte_Frimousse", "physique", "Electrik", 20)



#Pokemon stats + attaque

Pok1 = Pokemon("Salamèche", "Feu", None, 39, 56, 47, 60, 50, 65, Flammeche, Charge, None,None)
Pok2 = Pokemon("Reptincel", "Feu", None, 58, 64, 58, 80, 65, 80, Flammeche, Charge, None,Crocs_Feu)
Pok3 = Pokemon("Dracaufeu", "Feu", "Vol", 185, 149, 143, 177, 150, 167, Lanceflamme, None, Boutefeu, Tranche)
Pok4 = Pokemon("Carapuce", "Eau", None, 44, 48, 65, 50, 64, 43, Pistolet_a_O, None, Charge,None)
Pok5 = Pokemon("Carabaffe", "Eau", None, 59, 63, 80, 65, 80, 58, Pistolet_a_O, Morsure, Charge,None)
Pok6 = Pokemon("Tortank", "Eau", None, 186, 148, 167, 150, 172, 143, Vibraqua, Tour_rapide, Morsure, None)
Pok7 = Pokemon("Bulbizarre", "Plante", "Poison", 45, 49, 49, 65, 65, 45, None, Fouet_Lianes, None, Charge)
Pok8 = Pokemon("Herbizarre", "Plante", "Poison", 60, 62, 63, 80, 80, 60, Faux_Coup, Fouet_Lianes, None, Charge)
Pok9 = Pokemon("Florizarre", "Plante", "Poison", 187, 147, 148, 167, 167, 145, Bombe_Beurk, None, Damoclès,
               Coupe_feuille)
Pok10 = Pokemon("Pikachu", "Electrik", None, 35, 55, 40, 50, 50, 90, Éclair, Vive_Attaque, Frotte_Frimousse, Charge)

# Attaques potentielles pour chaque Pokemon
attaques_potentielles_Pok1 = [Crocs_Feu]
attaques_potentielles_Pok2 = [Damoclès]
attaques_potentielles_Pok3 = [Lame_dair]
attaques_potentielles_Pok4 = [Morsure]
attaques_potentielles_Pok5 = [Damoclès]
attaques_potentielles_Pok6 = [Hydro_queue]
attaques_potentielles_Pok7 = [Faux_Coup]
attaques_potentielles_Pok8 = [Damoclès]
attaques_potentielles_Pok9 = [Canon_graine]


# Assignation des attaques potentielles à chaque Pokemon
Pok1.attaques_potentielles = attaques_potentielles_Pok1
Pok2.attaques_potentielles = attaques_potentielles_Pok2
Pok3.attaques_potentielles = attaques_potentielles_Pok3
Pok4.attaques_potentielles = attaques_potentielles_Pok4
Pok5.attaques_potentielles = attaques_potentielles_Pok5
Pok6.attaques_potentielles = attaques_potentielles_Pok6
Pok7.attaques_potentielles = attaques_potentielles_Pok7
Pok8.attaques_potentielles = attaques_potentielles_Pok8
Pok9.attaques_potentielles = attaques_potentielles_Pok9

# Liste des Pokemons
pokemons = [Pok1, Pok2, Pok3, Pok4, Pok5, Pok6, Pok7, Pok8, Pok9]

# Chaque Pokemon gagne 4 combats
for pokemon in pokemons:
    for _ in range(4):
        pokemon.gagner_combat()  # Après ces combats, chaque Pokemon devrait apprendre une nouvelle attaque


def PokAttack(pok1, pok2, move):
    critChance = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1.5]
    randDamage = [85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    STABdmg = 1
    gamestate = 0
    if move.typ == pok1.type1:
        STABdmg = 1.5
    elif move.typ == pok1.type2:
        STABdmg = 1.5
    else:
        pass

    dmg = move.pwr

    if move.form == "Physique":
        damage = (((22 * dmg * (pok1.atk / pok2.df)) / 50) + 2) * random.choice(critChance) * (
            random.choice(randDamage)) * STABdmg
    else:
        damage = (((22 * dmg * (pok1.spatk / pok2.spdf)) / 50) + 2) * random.choice(critChance) * (
            random.choice(randDamage)) * STABdmg

    if move.typ == "Feu" and pok2.type1 == "Eau":
        damage *= 0.5
    if move.typ == "Feu" and pok2.type1 == "Plante":
        damage *= 1.8
    if move.typ == "Feu" and pok2.type1 == "Feu":
        damage *= 0.5
    if move.typ == "Plante" and pok2.type1 == "Eau":
        damage *= 1.8
    if move.typ == "Plante" and pok2.type1 == "Vol":
        damage *= 0.5
    if move.typ == "Plante" and pok2.type1 == "Plante":
        damage *= 0.5
    if move.typ == "Plante" and pok2.type1 == "Feu":
        damage *= 0.5
    if move.typ == "Eau" and pok2.type1 == "Eau":
        damage *= 0.5
    if move.typ == "Eau" and pok2.type1 == "Plante":
        damage *= 0.5
    if move.typ == "Eau" and pok2.type1 == "Feu":
        damage *= 1.8
    if move.typ == "Vol" and pok2.type1 == "Plante":
        damage *= 1.8
    if move.typ == "Electrik" and pok2.type1 == "Vol":
        damage *= 1.8
    if move.typ == "Electrik" and pok2.type1 == "Eau":
        damage *= 1.8

    damage = round(damage, 0)
    damage = int(damage / 100)

    print(f'{pok1.name} a utilisé {move.name}')
    pok2.hp -= damage
    print(f"{pok2.name} prend {damage} de dégat !")

    if pok2.hp <= 0:
        gamestate = 1
        pok2.hp = 0

    print(f'{pok2.name} a {pok2.hp} HP restant. \n')

    return gamestate

