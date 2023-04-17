#!/usr/bin/env python3
""" Index """
from models.pokemon import Pokemon
from api.v1.views import app_views
from models import storage
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"}), 200


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each objects by type """
    classes = {
        "pokemon": Pokemon,
    }

    num_objs = { num_objs[k]: storage.count(v) for k, v in classes.items() }

    return jsonify(num_objs), 200
