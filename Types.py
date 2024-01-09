class Types:
    def __init__(self, pokemons, moves):
        self.pokemons = pokemons  # Une liste de tous les Pokémon
        self.moves = moves  # Une liste de toutes les attaques

    def GaugeVie(self, pokemon):
        # Cette fonction retourne la jauge de vie du Pokémon
        return pokemon.hp

    def ComparatifCombat(self, pok1, pok2):
    # Cette fonction détermine quel Pokémon a l'avantage sur l'autre
    total_stats_pok1 = pok1.hp + pok1.atk + pok1.df + pok1.spatk + pok1.spdf + pok1.spd
    total_stats_pok2 = pok2.hp + pok2.atk + pok2.df + pok2.spatk + pok2.spdf + pok2.spd

    if total_stats_pok1 > total_stats_pok2:
        return f"{pok1.name} a l'avantage sur {pok2.name}"
    elif total_stats_pok1 < total_stats_pok2:
        return f"{pok2.name} a l'avantage sur {pok1.name}"
    else:
        return "Les deux Pokémon sont équivalents"



