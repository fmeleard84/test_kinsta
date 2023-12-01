
from flask import Flask, render_template, send_from_directory
#import connexion
#from agent_2 import agent_test_2
from test_fm import demo
from templates.test_fm_2 import demo2

#from agent.init_agent import agent_test
#from agent.init_agent import agent_test


app = Flask(__name__)

# Création de  l'instance de l'application
#app = connexion.App(__name__, specification_dir='./')

# Lecture du fichier swagger.yml pour définir les points d'arrivée (endpoints)
#app.add_api('swagger.yml')


# Dossier ou seront enregistrer les fichiers MP3 monté -> URL /montage

@app.route('/montage/<filename>')
def download_file(filename):
    return send_from_directory("audio/montage", filename)

@app.route('/demo2')
def agent_mail_2():

    agent = demo2()
    return agent

@app.route('/demo')
def agent_mail_1():

    agent = demo()
    return agent
# Url de test pour la partie Agent
#@app.route('/agent/mail')
#def agent_mail():

  #  agent = agent_test_2()
   # return agent

@app.route('/toto')
def test_fm():
    return render_template('home.html')

@app.route("/")
def home_view():
    return render_template('index.html')