import pathlib as pl

import numpy as np
import pandas as pd

from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

data = pl.Path(__file__).parent.absolute() / 'data'

# Charger les données CSV
associations_df = pd.read_csv(data / 'associations_etudiantes.csv')
evenements_df = pd.read_csv(data / 'evenements_associations.csv')

## Vous devez ajouter les routes ici : 

@app.route("/api/alive", methods=['GET'])
def alive():
    return { "message": "Alive" }

@app.route("/api/associations", methods=['GET'])
def assos():
    return list(associations_df['id'])

@app.route("/api/association/<int:id>", methods=['GET'])
def assos_spec(id):
    if id in list(associations_df['id']):
        return jsonify(associations_df[associations_df['id']==id].to_dict())
    return { "error": "Association not found" }, 404

@app.route("/api/evenements", methods=['GET'])
def evenements():
    return list(evenements_df['id'])

@app.route("/api/evenement/<int:id>", methods=['GET'])
def evenement_spec(id):
    if id in list(evenements_df['id']):
        return jsonify(evenements_df[evenements_df['id']==id].to_dict())
    return { "error": "Event not found" }, 404

@app.route("/api/association/<int:id>/evenements", methods=['GET'])
def assos_evenemnts(id):
    if id in list(associations_df['id']):
        return jsonify(evenements_df[evenements_df['association_id']==id].to_dict('split'))
    return { "error": "Association not found" }, 404

@app.route("/api/association/type/<type>", methods=['GET'])
def assos_type(type):
    return jsonify(associations_df[associations_df['type']==type].to_dict())

if __name__ == '__main__':
    app.run(debug=False)
