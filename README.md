🔍 Elasticsearch – Search & Analytics Evaluation Project

DataScientest | Data Engineering / Search Architecture

🎯 Contexte & objectif

Ce projet a été réalisé dans le cadre d’une évaluation technique Elasticsearch chez DataScientest.
Il met en situation un cas client e-commerce, spécialisé dans la vente de prêt-à-porter féminin, souhaitant :

analyser la pertinence de ses produits,

explorer les avis clients,

effectuer des recherches textuelles et analytiques performantes,

construire des indicateurs exploitables via Kibana.

L’objectif est de démontrer une maîtrise opérationnelle d’Elasticsearch, depuis l’ingestion de données jusqu’à l’analyse avancée et la visualisation.

🧠 Approche Data Engineer / Architecte Search

Le projet adopte une logique orientée moteur de recherche distribué :

Ingestion de données structurées (CSV)

Définition d’un mapping cohérent

Exploration et qualité des données

Analyses statistiques et agrégations

Requêtes avancées orientées décision

Visualisation via Kibana

Bien que réalisé sur un dataset réduit, le projet s’inscrit dans une logique scalable, conforme aux architectures Elasticsearch utilisées en production.

📦 Structure du livrable
1️⃣ bulk_script.py – Ingestion & indexation

Ce script permet de :

télécharger le dataset :

https://dst-de.s3.eu-west-3.amazonaws.com/elasticsearch_fr/datasets/Womens_Clothing.csv


créer l’index eval,

définir un mapping explicite,

ingérer les données dans Elasticsearch.

🎯 Objectif : simuler une pipeline d’ingestion contrôlée, base de tout moteur de recherche performant.

2️⃣ Scripts eval_elastic_x_y.py – Requêtes d’évaluation

Chaque script correspond à une question précise de l’évaluation.

Exécution unitaire possible :

python3 eval_elastic_1_1.py
python3 eval_elastic_2_3.py


À chaque exécution, un dossier est automatiquement généré pour l’examinateur :

/eval/questions/q_1-1/
├── mapping.json
├── request.json
├── response.json


mapping.json : structure de l’index

request.json : requête Elasticsearch

response.json : réponse brute du cluster

🎯 Objectif : garantir traçabilité, auditabilité et reproductibilité des analyses.

3️⃣ Qualité & exploration des données

Les requêtes couvrent :

valeurs uniques (Division Name, Department Name, Class Name)

volume total d’articles

cohérence des appartenances Division / Département

détection de valeurs nulles

🎯 Objectif : comprendre et fiabiliser la donnée avant toute analyse avancée.

4️⃣ Analyses statistiques & agrégations

Mise en œuvre de :

histogrammes (âge des clientes),

statistiques descriptives (moyenne, médiane des notes),

agrégations par classe de produit,

analyses croisées âge × type de produit.

🎯 Objectif : exploiter Elasticsearch comme moteur analytique temps réel, et pas uniquement comme moteur de recherche textuelle.

5️⃣ Analyses avancées orientées décision

Cette partie répond directement à des enjeux business :

termes les plus présents dans les produits bien notés,

termes associés aux produits mal notés,

identification des produits à conserver dans le catalogue,

détection des produits à faible valeur ajoutée.

🎯 Objectif : transformer la donnée en recommandations exploitables pour le client.

6️⃣ dashboard.png – Visualisations Kibana

4 visualisations intégrées dans un dashboard Kibana

Illustration de la capacité à industrialiser l’analyse via un outil BI temps réel

Approche proche d’un livrable client

7️⃣ Fichiers informatifs

create_index_eval.txt : détail du mapping et de la création de l’index

verification_index_eval.txt : vérification de l’existence et de la cohérence des index

🏗️ Architecture cible (projection production)

Bien que le projet soit réalisé en local, l’architecture est pensée pour évoluer vers :

ingestion automatisée via Logstash / Beats,

pipelines distribuées,

volumes de données massifs (millions de documents),

monitoring et observabilité Elasticsearch.

🧩 Compétences mises en œuvre

🔍 Elasticsearch (index, mapping, query DSL)

🐍 Python & client Elasticsearch

📊 Agrégations et statistiques avancées

🧠 Analyse textuelle orientée métier

📈 Kibana (dashboards & visualisations)

🏗️ Architecture Search & Analytics

📁 Structuration professionnelle des livrables
