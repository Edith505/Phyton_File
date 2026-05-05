from pathlib import Path
import argparse
import shutil

parser = argparse.ArgumentParser(description="copie partielle")

parser.add_argument("dossier", type=str)
parser.add_argument("nom_fichier", type=str)
parser.add_argument("nb_lignes", type=int)

args = parser.parse_args()

path = Path(args.dossier)

fichier_trouver = None

for racine, dossiers, fichiers in path.walk():
    for nom in fichiers:
        if nom == args.nom_fichier:
            fichier_trouver = racine / nom
            break
    if fichier_trouver:
        break
    
if not fichier_trouver:
    print('aucun fichier trouver')
    exit()

ligne_a_copier = []
with open(fichier_trouver,'r') as f:
    for i, ligne in enumerate(f):
        if i >= args.nb_lignes:
            break
        ligne_a_copier.append(ligne)
        
destination = Path(f"copie_{args.nom_fichier}")

with open(destination, 'w') as f:
    f.writelines(ligne_a_copier)
    
print("copie terminer :",destination) 


# =============== autre version ======================
fichier_trouver = None
for fichier in path.rglob(args.nom_fichier):
    fichier_trouver = fichier
    break

if not fichier_trouver:
    print('aucun fichier trouvé')
    exit()

# Lire les N premières lignes
ligne_a_copier = []
with open(fichier_trouver, 'r') as f:
    for i, ligne in enumerate(f):
        if i >= args.nb_lignes:
            break
        ligne_a_copier.append(ligne)

destination = Path(f"copie_{args.nom_fichier}")

# Écrire les lignes
with open(destination, 'w') as f:
    f.writelines(ligne_a_copier)

print("copie terminée :", destination)