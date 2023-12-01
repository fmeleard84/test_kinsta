
from flask import Flask, render_template, send_from_directory, url_for
import os

import connexion

app = Flask(__name__)

# Lecture du fichier swagger.yml pour définir les points d'arrivée (endpoints)
app.add_api('swagger.yml')

@app.route('/audio/montage/<filename>')
def download_file(filename):
    return send_from_directory("montage", filename)

@app.route("/")
def home_view():
    return render_template('index.html')
