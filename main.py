
taches = []

while True:
    print("\n===== GESTION DES TÂCHES =====")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Rechercher une tâche")
    print("4. Quitter")

    choix = input("Votre choix : ")

    if choix == "1":
        tache = input("Ajouter une tâche : ")
        taches.append(tache)
        print("Tâche ajoutée avec succès !")

    elif choix == "2":
        print("\nListe des tâches :")

        if len(taches) == 0:
            print("Aucune tâche disponible.")
        else:
            for i, tache in enumerate(taches, start=1):
                print(i, "-", tache)

    elif choix == "3":
        recherche = input("Nom de la tâche à rechercher : ")
        trouvee = False

        for tache in taches:
            if recherche.lower() in tache.lower():
                print("Tâche trouvée :", tache)
                trouvee = True

        if trouvee == False:
            print("Tâche introuvable.")

    elif choix == "4":
        print("Au revoir !")
        break

    else:
        print("Choix invalide. Réessayez.")
