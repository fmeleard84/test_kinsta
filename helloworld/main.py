
from flask import Flask, render_template, send_from_directory, url_for

app = Flask(__name__)

@app.route('/montage/<filename>')
def download_file(filename):
    return send_from_directory("montage", filename)

@app.route('/toto')
def test_fm():
    return render_template('home.html')

@app.route("/")
def home_view():
    return render_template('index.html')