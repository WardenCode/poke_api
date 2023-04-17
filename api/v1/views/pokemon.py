#!/usr/bin/env python3
""" objects that handles all default RestFul API actions for Amenities"""
from models.pokemon import Pokemon
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify


@app_views.route('/pokemon', methods=['GET'])
def get_pokemons():
    """
    Retrieves a list of all Pokemons
    """
    all_pokemons = storage.all(Pokemon).values()

    return jsonify([pokemon.to_dict() for pokemon in all_pokemons])


@app_views.route('/pokemon/<pokemon_id>', methods=['GET'])
def get_pokemon(pokemon_id):
    """ Retrieves an Pokemon """
    pokemon = storage.get(Pokemon, pokemon_id)
    if not pokemon:
        abort(404)

    return jsonify(pokemon.to_dict())
