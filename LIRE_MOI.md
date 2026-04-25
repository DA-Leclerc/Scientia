# SCIENTIA — Instructions de démarrage

## Installation (une seule fois)

Ouvre le Terminal et entre ces deux commandes :

```
pip install anthropic
export ANTHROPIC_API_KEY="ta-clé-ici"
```

Pour trouver ta clé API : https://console.anthropic.com/keys

Pour que la clé persiste après redémarrage :
```
echo 'export ANTHROPIC_API_KEY="ta-clé-ici"' >> ~/.zshrc
```

## Lancer SCIENTIA

Dans le Terminal, navigue vers ce dossier :
```
cd ~/Claude/Projets/scientia
python scientia.py
```

## Ce que ça fait

1. Tu choisis un concept statistique (ex. : "Moyenne et médiane")
2. Claude génère 5 questions adaptées à ton niveau
3. Tu réponds en texte libre
4. Claude évalue ta réponse et t'explique ce qui manque
5. Tes scores sont sauvegardés automatiquement

## Curriculum : 4 mois

- **Mois 1** : Fondations (population, variables, moyenne, écart-type, distribution normale, z-scores)
- **Mois 2** : Inférence (hypothèses, p-value, taille d'effet)
- **Mois 3** : Relations (corrélation, régression, R²)
- **Mois 4** : Psychométrie (analyse factorielle, héritabilité)

## Ingérer tes propres documents (Module 5)

Tu peux ajouter n'importe quel PDF, Markdown ou TXT au curriculum.
Scientia en extrait les concepts clés et les transforme en cartes de révision.

**Étapes :**
1. Installe pypdf si pas encore fait : `pip install pypdf`
2. Glisse ton fichier dans le dossier `docs/`
3. Lance Scientia → option **[3] Ingérer un document**
4. Sélectionne le fichier — Claude extrait 1 à 5 concepts automatiquement
5. Les nouveaux concepts apparaissent dans **[1] Étudier un concept → Module 5 "Documents personnels"**

Pour supprimer un concept ingéré : option **[4] Gérer les documents ingérés**.

Il y a un fichier `docs/test_challenge_point.md` (Challenge Point Framework) qui peut servir de premier test.
