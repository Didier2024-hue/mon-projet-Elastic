# 1. Supprimer l'index existant (si nécessaire)
DELETE /eval

# 2. Créer l'index avec la configuration finale
PUT /eval
{
  "settings": { ... },  // Reprendre la configuration complète ci-dessus
  "mappings": { ... }   // Idem
}

# 3. Importer les données
POST /_reindex
{
  "source": { "index": "source_index" },
  "dest": { "index": "eval" }
}