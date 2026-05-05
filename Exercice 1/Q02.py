def trouver_motif(chemin_fichier, motif):
    try:
        with open(chemin_fichier, "r") as f:
            for index_ligne, ligne in enumerate(f):
                index_colonne = ligne.find(motif)
                
                if index_colonne != -1:
                    return (index_ligne, index_colonne)
                
    except FileNotFoundError:
        print("fichier introuvable")

resultat = trouver_motif("Exercice 1/file.txt", "only")

if resultat:
    print("trouvé a : ", resultat)
    
else:
    print("Motif non trouvé")