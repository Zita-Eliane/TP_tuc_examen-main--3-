import requests
import random

base_url = "https://pokeapi.co/api/v2"


def get_pokemon_name(api_id):
    """
        Get a pokemon name from the API pokeapi
    """
    return get_pokemon_data(api_id)['name']

def get_pokemon_stats(api_id):
    """
        Get pokemon stats from the API pokeapi
    """
    stats_raw = get_pokemon_data(api_id)['stats']
    stats = dict()
    
    for stat in stats_raw:
        stats[stat['stat']['name']] = stat['base_stat']
    
    return stats

def get_pokemon_data(api_id):
    """
        Get data of pokemon name from the API pokeapi
    """
    return requests.get(f"{base_url}/pokemon/{api_id}", timeout=10).json()


def battle_pokemon(first_api_id, second_api_id):
    """
        Do battle between 2 pokemons
    """
    premierPokemon = get_pokemon_name(first_api_id)
    secondPokemon = get_pokemon_name(second_api_id)
    battle_result = battle_compare_stats(get_pokemon_stats(first_api_id), get_pokemon_stats(second_api_id))
    return {'winner': premierPokemon} if battle_result == 1 else {'winner': secondPokemon} if battle_result == 2 else {'winner': 'draw'} 


def battle_compare_stats(first_pokemon_stats, second_pokemon_stats):
    """
        Compare given stat between two pokemons
    """
    first_pokemon_total = 0
    second_pokemon_total = 0
    
    for key in first_pokemon_stats:
        if first_pokemon_stats[key] > second_pokemon_stats[key]: 
            first_pokemon_total+=1
        if first_pokemon_stats[key] < second_pokemon_stats[key]:
            second_pokemon_total+=1
        
    if first_pokemon_total > second_pokemon_total:
        return 1
    if first_pokemon_total < second_pokemon_total:
        return 2
    
    return 0


def generate_three_random_pokemon():
    """
        Return 3 random pokemon and their stats
    """
    pokelist = list()
    poke_id_list = random.sample(range(1,901), 3)
    for poke_id in poke_id_list:
        poke = dict()
        poke['name'] = get_pokemon_name(poke_id)
        poke['stats'] = get_pokemon_stats(poke_id)
        pokelist.append(poke)
    
    return pokelist


