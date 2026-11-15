# Projet : Rédiger le README.md du TP1

## Présentation
Ce TP a pour objectif de comprendre l'utilisation conjointe de Git et de Python à travers la création et l'évolution d'un script. Le fichier `main.py` est le script principal qui contient la logique du programme.

## Versions V1 à V4
- **Version 1 (V1) :** Le message initial de bienvenue, créé localement[cite: 5].
- **Version 2 (V2) :** L'ajout du prénom de l'utilisateur, puis le premier push vers GitHub[cite: 5].
- **Version 3 (V3) :** L'ajout de la matière à réviser sur GitHub, puis sa récupération avec `git pull`[cite: 5].
- **Version 4 (V4) :** L'ajout de la durée de révision sur le PC, puis le nouveau `git push`[cite: 5].

## Comment exécuter le programme
1. Ouvrir `TP_Git_Python` dans VS Code, puis cliquer sur `main.py`[cite: 5].
2. Cliquer sur **▶ Run Python File** en haut à droite de l’éditeur. Si nécessaire, choisir l’interpréteur Python[cite: 5].
3. Dans le terminal intégré qui s’ouvre, saisir le prénom, la matière et la durée en minutes. Valider chaque réponse avec **Entrée**[cite: 5].

## Commandes Git utilisées
- `git init` : Initialise un nouveau dépôt Git local dans le dossier du projet.
- `git add` : Ajoute les fichiers modifiés à l'espace de staging (zone de préparation avant le commit).
- `git commit` : Enregistre officiellement les modifications préparées dans l'historique du dépôt avec un message explicatif.
- `git push` : Envoie les commits locaux vers un dépôt distant (comme GitHub).
- `git pull` : Récupère et fusionne les dernières modifications du dépôt distant vers votre machine locale.