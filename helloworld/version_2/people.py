from datetime import datetime
 
def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Données sous-jacentes à l'API
PEOPLE = {
            "Dupont": {
                    "fname": "Jean",
                    "lname": "Dupont",
                    "timestamp": get_timestamp()
            },
            "Durand": {                
                    "fname": "Louise",
                    "lname": "Durand",
                    "timestamp": get_timestamp()
            },
            "Lopez": {
                    "fname": "Francois",
                    "lname": "Lopez",
                    "timestamp": get_timestamp()
            } 
}
            
# Création d'un handler read (GET) pour les données people
def read():
    # Création de la liste de personnes à partir de nos données
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]
