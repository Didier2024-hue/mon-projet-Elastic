#!/usr/bin/python
from elasticsearch import Elasticsearch
import json
import warnings
import os
import shutil  # Nouveau module pour supprimer des répertoires

# Désactivation des avertissements
warnings.filterwarnings("ignore")

# Connexion au cluster Elasticsearch
client = Elasticsearch(hosts="http://@localhost:9200")

# Numéro de la question (ex: "1-1", "2-3", etc.)
question_number = "1-2"  

# Chemin du répertoire pour la question
question_dir = f"./questions/q_{question_number}"

# --- Nettoyage du répertoire existant ---
if os.path.exists(question_dir):
    shutil.rmtree(question_dir)  # Supprime le répertoire et son contenu
    print(f"Ancien répertoire supprimé : {question_dir}")

# Création du nouveau répertoire
os.makedirs(question_dir, exist_ok=True)
print(f"Répertoire créé : {question_dir}")

# --- PARTIE 1: Sauvegarde du template de mapping ---
try:
    template = client.indices.get_mapping(index="eval")  # Spécifiez l'index si nécessaire
    with open(f"{question_dir}/mapping.json", "w") as f:
        json.dump(template, f, indent=2)
    print("Template de mapping sauvegardé.")
except Exception as e:
    print(f"Erreur lors de la récupération du template : {e}")

# --- PARTIE 2: Exécution de la requête et sauvegarde ---
query = {
  "query": {
    "bool": {
      "should": [
        { "range": { "Rating": { "lt": 3 } } },
        { "range": { "Positive Feedback Count": { "lt": 5 } } },
        { "term": { "Recommended IND": 0 } }
      ],
      "minimum_should_match": 1
    }
  },
  "sort": [
    { "Rating": { "order": "asc" } },
    { "Positive Feedback Count": { "order": "asc" } }
  ],
  "size": 100,
  "_source": ["Clothing ID", "Title", "Rating", "Recommended IND", "Department Name"]
}

try:
    response = client.search(index="eval", body=query)
    
    # Sauvegarde de la réponse
    with open(f"{question_dir}/response.json", "w") as f:
        json.dump(response, f, indent=2)
    
    # Sauvegarde de la requête
    with open(f"{question_dir}/request.json", "w") as f:
        json.dump(query, f, indent=2)
    
    print("Requête et réponse sauvegardées.")

except Exception as e:
    print(f"Erreur lors de l'exécution de la requête : {e}")

print(f"\nTraitement terminé. Données disponibles dans : {question_dir}")
