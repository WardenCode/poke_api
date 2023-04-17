#!/usr/bin/env python3
""" Starts a Flash Web Application """
from flask import Flask, render_template
from models import storage
from models.pokemon import Pokemon

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/', methods=["GET"])
def main_content():
    """ Print the main page """
    pokemons = []
    for pokemon in storage.session.query(Pokemon).all():
        filtered_stats = pokemon.stats.to_dict()
        del filtered_stats['id']
        del filtered_stats['__class__']
        setattr(pokemon, 'stat', filtered_stats)
        setattr(pokemon, 'abilities', pokemon.abilities)
        setattr(pokemon, 'types', pokemon.types)
        pokemons.append(pokemon)

    return render_template('main.html', pokemons=pokemons)


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
