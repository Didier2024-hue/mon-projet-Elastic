from elasticsearch import Elasticsearch, helpers
import csv
from collections import defaultdict

ES_HOST = "http://localhost:9200"
INDEX_NAME = "eval"
CSV_FILE = "Womens_Clothing.csv"

def setup_index(es):
    """Configure l'index avec les mappings nécessaires"""
    if es.indices.exists(index=INDEX_NAME):
        es.indices.delete(index=INDEX_NAME)
    
    mapping = {
        "properties": {
            "Clothing ID": {"type": "integer"},
            "Age": {"type": "integer"},
            "Title": {"type": "text"},
            "Review Text": {"type": "text"},
            "Rating": {"type": "integer"},
            "Recommended IND": {"type": "integer"},
            "Positive Feedback Count": {"type": "integer"},
            "Division Name": {"type": "keyword"},
            "Department Name": {"type": "keyword"},
            "Class Name": {"type": "keyword"},
            "Duplicate_Flag": {"type": "boolean"}
        }
    }
    es.indices.create(index=INDEX_NAME, mappings=mapping)

def process_file():
    """Lit le fichier CSV et prépare les données pour l'import"""
    with open(CSV_FILE, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        seen_ids = set()
        
        for row in reader:
            try:
                clothing_id = int(row["Clothing ID"])
                is_duplicate = clothing_id in seen_ids
                seen_ids.add(clothing_id)
                
                doc = {
                    "Clothing ID": clothing_id,
                    "Age": int(row["Age"]),
                    "Title": row["Title"],
                    "Review Text": row["Review Text"],
                    "Rating": int(row["Rating"]),
                    "Recommended IND": int(row["Recommended IND"]),
                    "Positive Feedback Count": int(row["Positive Feedback Count"]),
                    "Division Name": row["Division Name"],
                    "Department Name": row["Department Name"],
                    "Class Name": row["Class Name"],
                    "Duplicate_Flag": is_duplicate
                }
                
                yield {
                    "_index": INDEX_NAME,
                    "_source": doc
                }
                
            except (ValueError, KeyError) as e:
                print(f"Erreur traitement ligne: {e}")

def main():
    es = Elasticsearch(ES_HOST, request_timeout=60)
    
    if not es.ping():
        raise ConnectionError("Connexion Elasticsearch échouée")
    
    try:
        # Configuration de l'index
        setup_index(es)
        
        # Import des données
        success, errors = helpers.bulk(es, process_file(), stats_only=True)
        print(f"\nDocuments indexés: {success}, Erreurs: {errors}")
        
        # Vérification
        es.indices.refresh(index=INDEX_NAME)
        count = es.count(index=INDEX_NAME)['count']
        print(f"Total documents dans l'index: {count}")
        
        # Vérification des doublons
        duplicates = es.count(
            index=INDEX_NAME,
            body={"query": {"term": {"Duplicate_Flag": True}}}
        )['count']
        print(f"Documents marqués comme doublons: {duplicates}")
        
    finally:
        es.close()

if __name__ == "__main__":
    main()