from pathlib import Path
import shutil
import argparse

parser = argparse.ArgumentParser(description='Extraction et copie de motif dans un fichier')

parser.add_argument("dossier", help="dossier à explorer")
parser.add_argument("nom_fichier", help="le fichier à chercher")
parser.add_argument("motif", help="le texte à extraire")
parser.add_argument("destination", help="le dossier de sauvegard")

args = parser.parse_args()

path_source = Path(args.dossier)
path_destination = Path(args.destination)

if not path_source.exists:
    print("dossier l'existe pas")
    exit()

fichier_trouver = None
for fichier in path_source.rglob(args.nom_fichier):
    fichier_trouver = fichier
    break

if not fichier_trouver:
    print("le fichier n'a pas été trouver")
    exit()

try:
    with open(fichier_trouver, 'r') as f:
        contenu = f.read()
except Exception:
    print('erreur lors du lecture du fichier')
    exit()
    
if args.motif not in contenu:
    print("le contenu n'existe pas dans le fichier")
    exit()
    
motif_extrait = args.motif

print(f"Motif trouvé : '{motif_extrait}'")
print(f"Longueur : {len(motif_extrait)} caractères")

if not path_destination.exists():
    print("creation du dossier de destination")
    path_destination.mkdir(parents=True, exist_ok=True)
    
nom_fichier_sortie = f"extrait_{args.nom_fichier}"
path_fichier_sortie = path_destination / nom_fichier_sortie

print(f"Écriture du motif dans : {path_fichier_sortie}")

try:
    with open(path_fichier_sortie, "w") as f:
        f.write(motif_extrait)
except Exception:
    print(f"Erreur")
    exit()

print(f"\nOpération réussie !")
print(f" Fichier source : {fichier_trouver}")
print(f" Motif extrait : '{motif_extrait}'")
print(f" Fichier destination : {path_fichier_sortie}")