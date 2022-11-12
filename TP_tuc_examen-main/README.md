Groupe : 
    - Boutillier Paul
    - Looten Alexis
    - Vandewalle Axel
    - Amelete Mawaba Zita

Travail réalisé :
    - Endpoint crées : get.(/pokemons/battle),  get.(/pokemons/random), get.(/trainers/by_name/{trainer_name})
    - fonction compélétées : get_pokemon_stats() / battle_compare_stats() / battle_pokemon() dans le fichier app/utils/pokeapi.py
    - fonction modifiée : get_trainer_by_name()
    - fonction crée (groupe de 4) : get_three_random_pokemon()
    - Tests unitaire écrits : 7 --> voir test_unit.py
    - Tests mock écrits : 5 --> voir test_mick.py
    

Autres informations :
    - Coverage = 9O %
    - Score PyLint = 8.10/10
    - Locust scénario = 2 nouveaux joueurs créent leur compte, obtienent leur premier pokemon puis s'affrontent avec ces derniers.