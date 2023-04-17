#!/usr/bin/env python3
""" objects that handles all default RestFul API actions for Amenities"""
from models import storage
from models.abilities import Ability
from models.types import Type
from models.pokemon import Pokemon
from models.stats import Stat
from models.pokemon_type import PokemonTypeAssociation
from models.pokemon_ability import PokemonAbilityAssociation

from api.v1.views import app_views
from flask import abort, jsonify
from utils.poke_api import abilities_data, types_data, pokemon_data


@app_views.route('/update_db', methods=['GET'])
def update_db():
    """
    Clean and fill the database with Poke API data
    """
    storage.clean()

    abilities = [Ability(**ability) for ability in abilities_data()]
    types = [Type(**type) for type in types_data()]
    pokemons, stats, type_association, ability_association, = [], [], [], []

    storage.bulk_new(abilities)
    storage.bulk_new(types)

    for pokemon in pokemon_data():
        pokemon_types = pokemon.pop('types')
        pokemon_abilities = pokemon.pop('abilities')
        pokemon_stats = pokemon.pop('stats')

        stats.append(Stat(**pokemon_stats))
        pokemon_obj = Pokemon(**pokemon)

        for type in pokemon_types:
            (type_obj, _) = storage.get_or_create(Type, **type)
            pokemon_obj.types.append(type_obj)
            type_association.append(PokemonTypeAssociation(pokemon_id=pokemon_obj.id, type_id=type_obj.id))

        for ability in pokemon_abilities:
            (ability_obj, _) = storage.get_or_create(Ability, **ability)
            pokemon_obj.abilities.append(ability_obj)
            ability_association.append(PokemonAbilityAssociation(pokemon_id=pokemon_obj.id, ability_id=ability_obj.id))

        pokemons.append(pokemon_obj)

    storage.bulk_new(pokemons)
    storage.bulk_new(stats)
    storage.bulk_new(ability_association)
    storage.bulk_new(type_association)

    storage.save()

    return (jsonify({}), 200)
