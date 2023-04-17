#!/usr/bin/env python3
from requests import get
from os import getenv
from dotenv import load_dotenv

load_dotenv()

BASE_URL = getenv('API_URL')

def get_sprite(pokemon):
    return pokemon['sprites']['other']['official-artwork']['front_default']

def get_stats(pokemon):
    stats = pokemon['stats']
    result = {}

    result['id'] = pokemon['order']
    for data in stats:
        name = data['stat']['name'].replace('-', '_')
        base_stat = data['base_stat']

        result[name] = base_stat

    return result

def get_from_poke_api(data):
    return {
        'id': data['url'].split('/')[-2],
        'name': data['name'],
    }

def get_list_of(elements, key):
    return [get_from_poke_api(element[key]) for element in elements]

def get_pokemon(url):
    pokemon_data = get(url).json()
    new_pokemon = {
        'id': pokemon_data['order'],
        'order': pokemon_data['order'],
        'name': pokemon_data['name'],
        'types': get_list_of(pokemon_data['types'], 'type'),
        'abilities': get_list_of(pokemon_data['abilities'], 'ability'),
        'height': pokemon_data['height'],
        'weight': pokemon_data['weight'],
        'base_experience': pokemon_data['base_experience'],
        'stats': get_stats(pokemon_data),
        'sprite': get_sprite(pokemon_data),
    }

    return new_pokemon

def pokemon_data():
    # request = get(f'{BASE_URL}/pokemon?offset=0&limit=10000')
    # request = get(f'{BASE_URL}/pokemon?offset=0&limit=151')
    request = get(f'{BASE_URL}/pokemon?offset=0&limit=10')
    data = request.json()
    results = data.get('results')

    return [get_pokemon(pokemon['url']) for pokemon in results]

def abilities_data():
    request = get(f'{BASE_URL}/ability?offset=0&limit=10000')
    data = request.json()
    results = data.get('results')

    return [get_from_poke_api(ability) for ability in results]

def types_data():
    request = get(f'{BASE_URL}/type?offset=0&limit=10000')
    data = request.json()
    results = data.get('results')

    return [get_from_poke_api(type) for type in results]
