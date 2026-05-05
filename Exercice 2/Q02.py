import argparse
from pathlib import Path

parser = argparse.ArgumentParser(prog="lecture fichier")
parser.add_argument('source', help="source du fichier")

args = parser.parse_args()

path = Path(args.source)

total_fichiers = 0
taille_totale = 0
plus_gros = ("", 0)

for fichier in path.rglob('*'):
    if fichier.is_file():
        total_fichiers += 1
        taille = fichier.stat().st_size
        taille_totale += taille
        
        if taille > plus_gros[1]:
            plus_gros = (fichier.name, taille)
            