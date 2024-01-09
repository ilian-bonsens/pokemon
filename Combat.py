import random


class Pokemon:
    def __init__(self, name, type1, type2, hp, atk, df, spatk, spdf, spd, move1, move2, move3, move4):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp
        self.atk = atk
        self.df = df
        self.spatk = spatk
        self.spdf = spdf
        self.spd = spd
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4


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
Morsure = Move("Morcure", "Physique", "Dark", 60)
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

#Pokemon stats + attaque

Pok1 = Pokemon("Salamèche", "Feu", None, 39, 56, 47, 60, 50, 65, Flammeche, Charge, Damoclès,Crocs_Feu)
Pok2 = Pokemon("Reptincel", "Feu", None, 58, 64, 58, 80, 65, 80, Flammeche, Charge, Damoclès,Crocs_Feu)
Pok3 = Pokemon("Dracaufeu", "Feu", "Vol", 185, 149, 143, 177, 150, 167, Lanceflamme, Lame_dair, Boutefeu, Tranche)
Pok4 = Pokemon("Carapuce", "Eau", None, 44, 48, 65, 50, 64, 43, Pistolet_a_O, Morsure, Charge,Damoclès)
Pok5 = Pokemon("Carabaffe", "Eau", None, 59, 63, 80, 65, 80, 58, Pistolet_a_O, Morsure, Charge,Damoclès)
Pok6 = Pokemon("Tortank", "Eau", None, 186, 148, 167, 150, 172, 143, Vibraqua, Hydro_queue, Morsure, Tour_rapide)
Pok7 = Pokemon("Bulbizarre", "Plante", "Poison", 45, 49, 49, 65, 65, 45, Faux_Coup, Fouet_Lianes, Damoclès, Charge)
Pok8 = Pokemon("Herbizarre", "Plante", "Poison", 60, 62, 63, 80, 80, 60, Faux_Coup, Fouet_Lianes, Damoclès, Charge)
Pok9 = Pokemon("Florizarre", "Plante", "Poison", 187, 147, 148, 167, 167, 145, Canon_graine, Bombe_Beurk, Damoclès,
               Coupe_feuille)

