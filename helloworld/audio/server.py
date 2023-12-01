from flask import render_template, send_from_directory, url_for
import os

import connexion



# Création de  l'instance de l'application
app = connexion.App(__name__, specification_dir='./')

# Lecture du fichier swagger.yml pour définir les points d'arrivée (endpoints)
app.add_api('swagger.yml')
app.debug = True


# Configurez ici le chemin absolu vers votre dossier "montage"
#MONTAGE_FOLDER = os.path.abspath("/audio")
#print (MONTAGE_FOLDER)

# The code below lets the Flask server respond to browser requests for a favicon
@app.route("/favicon.ico")
def favicon():
    return url_for('static', filename='data:,')

@app.route('/montage/<filename>')
def download_file(filename):
    return send_from_directory("montage", filename)


# Création d'une URL pour "/"
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
