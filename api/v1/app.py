#!/usr/bin/env python3

from flask import Flask, jsonify, make_response
from flask_cors import CORS
from models import storage
from os import getenv
from api.v1.views import app_views

HOST: str = getenv('HOST') or 'localhost'
PORT: int = int(getenv('PORT') or '8080')

app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)

@app.route('/', methods=['GET'])
def min():
    return (jsonify({}), 200)

if (__name__ == '__main__'):
    app.run(host=HOST, port=PORT, debug=True)