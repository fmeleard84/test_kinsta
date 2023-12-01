from flask import render_template
import connexion
 
# Création de  l'instance de l'application
app = connexion.App(__name__, specification_dir='./')

# Lecture du fichier swagger.yml pour définir les points d'arrivée (endpoints)
app.add_api('swagger.yml')

# Création d'une URL pour "/"
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
