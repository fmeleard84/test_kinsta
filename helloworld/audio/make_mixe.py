import os
import random
from pydub import AudioSegment
import requests

# Recupere un MP3 d'une url de PUT
# Va chercher une bande son aleatoire dans le dossier musique
# Mixe les 2 avec 4 seconde de son, puis la voix off puis un fde out de 8s
# Site de référence -> https://datascientest.com/programmer-et-documenter-une-api-avec-python-flask-swagger-et-connexion
# Exemple de requette entrante -> http://38.180.62.251:8080/api/make_mixe?url=truc&name=bateau
# Exemple de requette de Donwload -> http://38.180.62.251:8080/montage/bateau.mp3
def download_mp3(url, output_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_path, 'wb') as f:
            f.write(response.content)
        return output_path
    else:
        return None

def mix_audio_tracks(voice_track_path, music_track_path, output_path):
    voice_track = AudioSegment.from_file(voice_track_path)
    music_track = AudioSegment.from_file(music_track_path)

    # 1. Démarrer la piste de musique 8 secondes avant la piste de voix
    silence = AudioSegment.silent(duration=5000)
    voice_track = silence + voice_track

    # 2. Terminer la piste de musique 8 secondes après la piste voix
    silence = AudioSegment.silent(duration=8000)
    voice_track = voice_track + silence

    # 3. Ajuster la longueur de la piste de musique pour qu'elle corresponde à la piste de voix
    if len(music_track) > len(voice_track):
        music_track = music_track[:len(voice_track)]
    else:
        silence = AudioSegment.silent(duration=(len(voice_track) - len(music_track)))
        music_track = music_track + silence

    # 4. Terminer la piste de musique en fade out sur les 4 dernières secondes
    music_track = music_track.fade_out(8000)

    # Mixage des deux pistes
    mixed = voice_track.overlay(music_track)
    mixed.export(output_path, format="mp3")
    return output_path

def random_audio_file(directory):
    audio_files = [f for f in os.listdir(directory) if f.endswith('.mp3')]
    if not audio_files:
        return None
    return os.path.join(directory, random.choice(audio_files))

def start(url,name):
    download_directory = "source"
    audio_directory = "musique"
    output_directory = "montage"

    base_url = "http://38.180.62.251:8080/api/make_mixe/montage/"
    output_url = os.path.join(base_url, f"{name}.mp3")

    output_url = name

    # Étape 1: Télécharger le fichier MP3
    mp3_path = download_mp3(url, os.path.join(download_directory, "downloaded.mp3"))
    if mp3_path is None:
        print("Échec du téléchargement du fichier MP3.")
        return

    # Étape 2: Sélectionner une piste audio aléatoire
    random_track_path = random_audio_file(audio_directory)
    if random_track_path is None:
        print("Aucun fichier audio trouvé dans le répertoire spécifié.")
        return

    # Étape 3: Mixer les deux pistes audio
    output_path = mix_audio_tracks(mp3_path, random_track_path, os.path.join(output_directory, f"{name}.mp3"))

    # Étape 4: Retourner l'URL de la piste audio mixée
    print("Piste audio mixée disponible à : {}".format(os.path.join(output_url, "mixed.mp3")))

    return {"url": output_path}